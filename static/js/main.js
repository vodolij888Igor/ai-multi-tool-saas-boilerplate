// Main JavaScript for AI Content Generator

// Theme Toggle
document.addEventListener('DOMContentLoaded', function() {
    // Initialize theme from localStorage
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-bs-theme', savedTheme);
    updateThemeIcon(savedTheme);
    
    // Theme toggle button
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.body.getAttribute('data-bs-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.body.setAttribute('data-bs-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }
    
    // Niche selection
    let selectedNiche = null;
    
    // Check if we're on a tool page (has hidden input with niche id)
    const hiddenNicheInput = document.getElementById('selectedNiche');
    if (hiddenNicheInput && hiddenNicheInput.type === 'hidden') {
        selectedNiche = hiddenNicheInput.value;
    } else {
        // Only handle niche selection on main page (not tool pages)
        const nicheCards = document.querySelectorAll('.niche-card');
        nicheCards.forEach(card => {
            card.addEventListener('click', function(e) {
                // Don't navigate if clicking on a link
                if (e.target.closest('a')) {
                    return;
                }
                
                e.preventDefault();
                e.stopPropagation();
                
                // Remove previous selection
                nicheCards.forEach(c => c.classList.remove('selected'));
                
                // Add selection to clicked card
                this.classList.add('selected');
                selectedNiche = this.dataset.niche;
                
                // Update form
                const nicheName = this.querySelector('.card-title').textContent;
                const nicheInput = document.getElementById('selectedNiche');
                if (nicheInput && nicheInput.type !== 'hidden') {
                    nicheInput.value = nicheName;
                }
            });
        });
    }
    
    // Зберігаємо niche для подальшого використання
    let currentNiche = null;
    
    // Form submission
    const contentForm = document.getElementById('contentForm');
    if (contentForm) {
        contentForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            // Get tool_name from hidden input if on tool page (Professional AI Tools)
            const selectedToolNameInput = document.getElementById('selectedToolName');
            let toolNameToUse = null;
            
            if (selectedToolNameInput) {
                toolNameToUse = selectedToolNameInput.value;
            }
            
            // Get niche from hidden input if on tool page (Personal & Creative Tools), otherwise from selectedNiche
            const currentNicheInput = document.getElementById('selectedNiche');
            let nicheToUse = null;
            
            if (currentNicheInput) {
                if (currentNicheInput.type === 'hidden') {
                    // On tool page - use hidden input value
                    nicheToUse = currentNicheInput.value;
                } else {
                    // On main page - use selected niche
                    nicheToUse = selectedNiche || currentNicheInput.value;
                }
            } else {
                nicheToUse = selectedNiche;
            }
            
            // Validate that we have either tool_name or niche
            if (!toolNameToUse && !nicheToUse) {
                showAlert('Будь ласка, оберіть інструмент', 'warning');
                return;
            }
            
            // Зберігаємо для подальшого використання
            currentNiche = nicheToUse;
            
            const userPrompt = document.getElementById('userPrompt').value;
            
            if (!userPrompt) {
                showAlert('Будь ласка, введіть запит', 'warning');
                return;
            }
            
            // Show loading
            showLoading(true);
            hideResults();
            
            try {
                // Build request body with tool_name (priority) or niche
                const requestBody = {
                    prompt: userPrompt
                };
                
                if (toolNameToUse) {
                    requestBody.tool_name = toolNameToUse;
                } else if (nicheToUse) {
                    requestBody.niche = nicheToUse;
                }
                
                const response = await fetch('/api/generate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(requestBody)
                });
                
                const data = await response.json();
                
                if (data.success) {
                    showResults(data.content, nicheToUse);
                } else {
                    showAlert(data.error || 'Помилка при генерації контенту', 'danger');
                }
            } catch (error) {
                showAlert('Помилка з\'єднання з сервером: ' + error.message, 'danger');
            } finally {
                showLoading(false);
            }
        });
    }
    
    // Copy button
    const copyBtn = document.getElementById('copyBtn');
    if (copyBtn) {
        copyBtn.addEventListener('click', function() {
            const content = document.getElementById('generatedContent').textContent;
            navigator.clipboard.writeText(content).then(function() {
                showAlert('Контент скопійовано в буфер обміну!', 'success');
                
                // Update button icon temporarily
                const icon = this.querySelector('i');
                const originalClass = icon.className;
                icon.className = 'bi bi-check';
                setTimeout(() => {
                    icon.className = originalClass;
                }, 2000);
            }.bind(this)).catch(function(err) {
                showAlert('Помилка копіювання: ' + err, 'danger');
            });
        });
    }
});

function updateThemeIcon(theme) {
    const themeIcon = document.getElementById('themeIcon');
    if (themeIcon) {
        if (theme === 'dark') {
            themeIcon.className = 'bi bi-sun';
        } else {
            themeIcon.className = 'bi bi-moon-stars';
        }
    }
}

function showLoading(show) {
    const loadingSpinner = document.getElementById('loadingSpinner');
    const generateBtn = document.getElementById('generateBtn');
    
    if (loadingSpinner) {
        loadingSpinner.style.display = show ? 'block' : 'none';
    }
    
    if (generateBtn) {
        generateBtn.disabled = show;
        const locale = document.documentElement.lang || 'uk';
        if (show) {
            const loadingText = locale === 'uk' ? 'Генерується...' : 
                               locale === 'en' ? 'Generating...' : 
                               'Generando...';
            generateBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>' + loadingText;
        } else {
            const generateText = locale === 'uk' ? 'Згенерувати' : 
                                locale === 'en' ? 'Generate' : 
                                'Generar';
            generateBtn.innerHTML = '<i class="bi bi-lightning-charge"></i> ' + generateText;
        }
    }
}

function showResults(content, toolType = null) {
    const resultsSection = document.getElementById('resultsSection');
    const generatedContent = document.getElementById('generatedContent');
    const saveButtonContainer = document.getElementById('saveButtonContainer');
    
    if (resultsSection && generatedContent) {
        // Відображаємо контент з підтримкою переносів рядків
        let contentHtml = content.replace(/\n/g, '<br>');
        generatedContent.innerHTML = contentHtml;
        
        // Показуємо кнопку "Save to Library" якщо вона існує (для tool.html)
        if (saveButtonContainer) {
            saveButtonContainer.style.display = 'block';
            // Зберігаємо toolType в data-атрибуті для подальшого використання
            saveButtonContainer.setAttribute('data-niche', toolType || '');
            // Додаємо обробник події для кнопки
            const saveToLibraryBtn = document.getElementById('saveToLibraryBtn');
            if (saveToLibraryBtn) {
                // Видаляємо старі обробники
                const newBtn = saveToLibraryBtn.cloneNode(true);
                saveToLibraryBtn.parentNode.replaceChild(newBtn, saveToLibraryBtn);
                // Додаємо новий обробник
                newBtn.addEventListener('click', saveToLibrary);
            }
        }
        
        // Додаємо кнопку "Зберегти як план дій" для головної сторінки (якщо немає saveButtonContainer)
        if (!saveButtonContainer) {
            const locale = document.documentElement.lang || 'uk';
            const saveText = locale === 'uk' ? 'Зберегти як план дій' : 
                            locale === 'en' ? 'Save as Action Plan' : 
                            'Guardar como Plan de Acción';
            
            // Видаляємо стару кнопку, якщо вона існує
            const oldBtn = document.getElementById('saveAsPlanBtn');
            if (oldBtn && oldBtn.parentElement) {
                oldBtn.parentElement.remove();
            }
            
            // Створюємо контейнер для кнопки
            const buttonContainer = document.createElement('div');
            buttonContainer.className = 'mt-3 text-center';
            buttonContainer.innerHTML = `
                <button type="button" class="btn btn-primary btn-lg" id="saveAsPlanBtn">
                    <i class="bi bi-bookmark-plus"></i> ${saveText}
                </button>
            `;
            
            // Додаємо обробник події
            const saveBtn = buttonContainer.querySelector('#saveAsPlanBtn');
            saveBtn.addEventListener('click', saveAsPlan);
            
            // Додаємо кнопку в card-body після generatedContent
            const cardBody = generatedContent.closest('.card-body');
            if (cardBody) {
                cardBody.appendChild(buttonContainer);
            } else {
                // Якщо немає card-body, додаємо після generatedContent
                generatedContent.parentElement.appendChild(buttonContainer);
            }
        }
        
        resultsSection.style.display = 'block';
        resultsSection.classList.add('fade-in');
        
        // Scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

async function saveAsPlan() {
    const generatedContent = document.getElementById('generatedContent');
    if (!generatedContent) return;
    
    // Отримуємо текст контенту (без HTML)
    const contentText = generatedContent.textContent || generatedContent.innerText;
    
    // Питаємо назву проекту
    const locale = document.documentElement.lang || 'uk';
    const titlePrompt = locale === 'uk' ? 'Введіть назву плану:' : 
                       locale === 'en' ? 'Enter plan title:' : 
                       'Ingrese el título del plan:';
    
    const title = prompt(titlePrompt);
    if (!title || !title.trim()) {
        return;
    }
    
    // Показуємо індикатор завантаження
    const saveBtn = document.getElementById('saveAsPlanBtn');
    const originalBtnText = saveBtn.innerHTML;
    saveBtn.disabled = true;
    saveBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>' + 
                       (locale === 'uk' ? 'Збереження...' : 
                        locale === 'en' ? 'Saving...' : 
                        'Guardando...');
    
    try {
        const response = await fetch('/dashboard/project/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: title.trim(),
                content: contentText
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            const successMsg = locale === 'uk' ? 'План успішно збережено! Переглянути в кабінеті.' : 
                             locale === 'en' ? 'Plan saved successfully! View in dashboard.' : 
                             '¡Plan guardado exitosamente! Ver en el panel.';
            showAlert(successMsg, 'success');
            
            // Оновлюємо кнопку
            saveBtn.innerHTML = '<i class="bi bi-check-circle"></i> ' + 
                               (locale === 'uk' ? 'Збережено' : 
                                locale === 'en' ? 'Saved' : 
                                'Guardado');
            setTimeout(() => {
                saveBtn.innerHTML = originalBtnText;
                saveBtn.disabled = false;
            }, 2000);
        } else {
            showAlert(data.error || 'Помилка збереження', 'danger');
            saveBtn.innerHTML = originalBtnText;
            saveBtn.disabled = false;
        }
    } catch (error) {
        showAlert('Помилка з\'єднання: ' + error.message, 'danger');
        saveBtn.innerHTML = originalBtnText;
        saveBtn.disabled = false;
    }
}

function hideResults() {
    const resultsSection = document.getElementById('resultsSection');
    if (resultsSection) {
        resultsSection.style.display = 'none';
        // Видаляємо кнопку збереження, якщо вона існує
        const saveBtn = document.getElementById('saveAsPlanBtn');
        if (saveBtn && saveBtn.parentElement) {
            saveBtn.parentElement.remove();
        }
        // Ховаємо кнопку "Save to Library"
        const saveButtonContainer = document.getElementById('saveButtonContainer');
        if (saveButtonContainer) {
            saveButtonContainer.style.display = 'none';
        }
    }
}

// Функція для збереження в бібліотеку
async function saveToLibrary() {
    const saveToLibraryBtn = document.getElementById('saveToLibraryBtn');
    if (!saveToLibraryBtn) return;
    
    const generatedContent = document.getElementById('generatedContent');
    const saveButtonContainer = document.getElementById('saveButtonContainer');
    
    if (!generatedContent) return;
    
    // Отримуємо текст контенту (без HTML)
    const contentText = generatedContent.textContent || generatedContent.innerText;
    
    // Отримуємо niche з data-атрибуту або зі збереженої змінної
    const niche = saveButtonContainer ? saveButtonContainer.getAttribute('data-niche') : null;
    
    // Питаємо назву проекту
    const locale = document.documentElement.lang || 'uk';
    const titlePrompt = locale === 'uk' ? 'Введіть назву проекту:' : 
                       locale === 'en' ? 'Enter project title:' : 
                       'Ingrese el título del proyecto:';
    
    const title = prompt(titlePrompt);
    if (!title || !title.trim()) {
        return;
    }
    
    // Показуємо індикатор завантаження
    const originalBtnText = saveToLibraryBtn.innerHTML;
    saveToLibraryBtn.disabled = true;
    saveToLibraryBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>' + 
                   (locale === 'uk' ? 'Збереження...' : 
                    locale === 'en' ? 'Saving...' : 
                    'Guardando...');
    
    try {
        const response = await fetch('/api/save_project', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: title.trim(),
                content: contentText,
                niche: niche || ''
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            const successMsg = locale === 'uk' ? 'Проект успішно збережено в бібліотеку!' : 
                             locale === 'en' ? 'Project saved to library successfully!' : 
                             '¡Proyecto guardado en la biblioteca exitosamente!';
            alert(successMsg);
            
            // Оновлюємо кнопку
            saveToLibraryBtn.innerHTML = '<i class="bi bi-check-circle"></i> ' + 
                                       (locale === 'uk' ? 'Збережено' : 
                                        locale === 'en' ? 'Saved' : 
                                        'Guardado');
            setTimeout(() => {
                saveToLibraryBtn.innerHTML = originalBtnText;
                saveToLibraryBtn.disabled = false;
            }, 2000);
        } else {
            alert(data.error || 'Помилка збереження');
            saveToLibraryBtn.innerHTML = originalBtnText;
            saveToLibraryBtn.disabled = false;
        }
    } catch (error) {
        alert('Помилка з\'єднання: ' + error.message);
        saveToLibraryBtn.innerHTML = originalBtnText;
        saveToLibraryBtn.disabled = false;
    }
}

// Обробник для кнопки "Save to Library" (використовуємо делегування подій)
document.addEventListener('DOMContentLoaded', function() {
    // Використовуємо делегування подій для динамічно створених кнопок
    document.addEventListener('click', function(e) {
        if (e.target && e.target.id === 'saveToLibraryBtn') {
            e.preventDefault();
            saveToLibrary();
        }
        // Також обробляємо клік на іконці всередині кнопки
        if (e.target && e.target.closest('#saveToLibraryBtn')) {
            e.preventDefault();
            saveToLibrary();
        }
    });
});
            const generatedContent = document.getElementById('generatedContent');
            const saveButtonContainer = document.getElementById('saveButtonContainer');
            
            if (!generatedContent) return;
            
            // Отримуємо текст контенту (без HTML)
            const contentText = generatedContent.textContent || generatedContent.innerText;
            
            // Отримуємо niche з data-атрибуту або зі збереженої змінної
            const niche = saveButtonContainer ? saveButtonContainer.getAttribute('data-niche') : null;
            
            // Питаємо назву проекту
            const locale = document.documentElement.lang || 'uk';
            const titlePrompt = locale === 'uk' ? 'Введіть назву проекту:' : 
                               locale === 'en' ? 'Enter project title:' : 
                               'Ingrese el título del proyecto:';
            
            const title = prompt(titlePrompt);
            if (!title || !title.trim()) {
                return;
            }
            
            // Показуємо індикатор завантаження
            const originalBtnText = this.innerHTML;
            this.disabled = true;
            this.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>' + 
                           (locale === 'uk' ? 'Збереження...' : 
                            locale === 'en' ? 'Saving...' : 
                            'Guardando...');
            
            try {
                const response = await fetch('/api/save_project', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        title: title.trim(),
                        content: contentText,
                        niche: niche || ''
                    })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    const successMsg = locale === 'uk' ? 'Проект успішно збережено в бібліотеку!' : 
                                     locale === 'en' ? 'Project saved to library successfully!' : 
                                     '¡Proyecto guardado en la biblioteca exitosamente!';
                    alert(successMsg);
                    
                    // Оновлюємо кнопку
                    this.innerHTML = '<i class="bi bi-check-circle"></i> ' + 
                                   (locale === 'uk' ? 'Збережено' : 
                                    locale === 'en' ? 'Saved' : 
                                    'Guardado');
                    setTimeout(() => {
                        this.innerHTML = originalBtnText;
                        this.disabled = false;
                    }, 2000);
                } else {
                    alert(data.error || 'Помилка збереження');
                    this.innerHTML = originalBtnText;
                    this.disabled = false;
                }
            } catch (error) {
                alert('Помилка з\'єднання: ' + error.message);
                this.innerHTML = originalBtnText;
                this.disabled = false;
            }
        });
    }
});

function showAlert(message, type) {
    // Remove existing alerts
    const existingAlerts = document.querySelectorAll('.alert-custom');
    existingAlerts.forEach(alert => alert.remove());
    
    // Create new alert
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show alert-custom`;
    alertDiv.setAttribute('role', 'alert');
    alertDiv.style.position = 'fixed';
    alertDiv.style.top = '80px';
    alertDiv.style.right = '20px';
    alertDiv.style.zIndex = '9999';
    alertDiv.style.minWidth = '300px';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(alertDiv);
    
    // Auto dismiss after 5 seconds
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

