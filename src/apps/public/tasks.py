import logging
from django.core.mail import send_mail
from django_q.tasks import async_task
from config import settings


logger = logging.getLogger(__name__)

def handler_send_notif_to_admins(fullname, email):
    logger.info("Handler function called")
    subject = 'New Contact Form Submission'
    message = f'You have received a new contact form submission.\n\nName: {fullname}\nEmail: {email}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, recipient_list)

def send_notif_to_admins(fullname, email):
    async_task(handler_send_notif_to_admins, fullname=fullname, email=email)