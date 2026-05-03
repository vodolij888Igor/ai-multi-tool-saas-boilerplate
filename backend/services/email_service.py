"""
Email service stub. Enable via FEATURE_EMAIL; implement with SendGrid, SMTP, etc.
"""
from config.feature_flags import FEATURE_EMAIL


def send_welcome_email(to_email: str, **kwargs) -> bool:
    if not FEATURE_EMAIL:
        return False
    # TODO: implement
    return False


def send_password_reset(to_email: str, reset_link: str, **kwargs) -> bool:
    if not FEATURE_EMAIL:
        return False
    # TODO: implement
    return False
