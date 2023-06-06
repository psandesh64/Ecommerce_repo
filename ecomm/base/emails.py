from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email, email_token):
    subject = 'Your accounts need to be verified'
    message = f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    email_from = settings.EMAIL_HOST_USER
    print(subject,message,email_from)
    send_mail(subject, message, email_from, [email])