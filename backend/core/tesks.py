from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from backend.celery import app
from users.models import User


@app.task
def send_confirmation_email(email, confirmation_code):
    """
    Task for Celery.
    Function sends emil with conformation code.
    """
    html_content = render_to_string(
        'confirmation_email.html',
        {'confirmation_code': confirmation_code}
    )
    msg = EmailMultiAlternatives(
        'Confirmation Code Email',
        '',
        'noreply@otomari.ru',
        (email,)
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    return 'Success'


@app.task
def delete_expired_2fa_code(user_id):
    """
    Task for Celery.
    Function deletes expired conformation code.
    """
    user = User.objects.get(id=user_id)
    user.confirmation_code = ''
    user.save()
    return 'Success'
