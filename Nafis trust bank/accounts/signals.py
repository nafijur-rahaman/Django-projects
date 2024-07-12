from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

User = get_user_model()

@receiver(post_save, sender=User)
def send_account_creation_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Site'
        template = 'accounts/account_created.html'
        message = render_to_string(template, {'user': instance})
        send_email = EmailMultiAlternatives(subject, '', to=[instance.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    subject = 'Login Notification'
    template = 'accounts/login_notification.html'
    message = render_to_string(template, {'user': user})
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()
