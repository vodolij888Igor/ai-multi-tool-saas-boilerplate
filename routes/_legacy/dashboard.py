"""
Роути для Dashboard користувача
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from extensions import db
from models import UserProject
from datetime import datetime

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    """Dashboard користувача з проектами"""
    projects = UserProject.query.filter_by(user_id=current_user.id).order_by(
        UserProject.date_created.desc()
    ).all()
    
    return render_template('dashboard.html', projects=projects, current_user=current_user)

@dashboard_bp.route('/dashboard/project/save', methods=['POST'])
@login_required
def save_project():
    """Збереження проекту з генерації"""
    try:
        data = request.get_json()
        title = data.get('title', '').strip()
        content = data.get('content', '').strip()
        
        if not title or not content:
            return jsonify({'success': False, 'error': 'Заповніть всі поля'}), 400
        
        project = UserProject(
            user_id=current_user.id,
            title=title,
            content=content
        )
        
        db.session.add(project)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'План успішно збережено!',
            'project_id': project.id
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@dashboard_bp.route('/dashboard/project/<int:project_id>/toggle', methods=['POST'])
@login_required
def toggle_project(project_id):
    """Перемикання статусу виконання проекту"""
    project = UserProject.query.get_or_404(project_id)
    
    # Перевірка, чи проект належить користувачу
    if project.user_id != current_user.id:
        flash('Немає доступу до цього проекту', 'danger')
        return redirect(url_for('dashboard.dashboard'))
    
    project.is_completed = not project.is_completed
    db.session.commit()
    
    flash('Статус проекту оновлено', 'success')
    return redirect(url_for('dashboard.dashboard'))

@dashboard_bp.route('/dashboard/project/<int:project_id>/delete', methods=['POST'])
@login_required
def delete_project(project_id):
    """Видалення проекту"""
    project = UserProject.query.get_or_404(project_id)
    
    # Перевірка, чи проект належить користувачу
    if project.user_id != current_user.id:
        flash('Немає доступу до цього проекту', 'danger')
        return redirect(url_for('dashboard.dashboard'))
    
    db.session.delete(project)
    db.session.commit()
    
    flash('Проект успішно видалено', 'success')
    return redirect(url_for('dashboard.dashboard'))

