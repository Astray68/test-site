from django.core.mail import EmailMessage
from MyTestWebsite.celery import app


@app.task
def send_mail_alert(subject, message, email_from, reply_to_list):
    msg = EmailMessage(subject, message, email_from, reply_to_list)
    msg.content_subtype = 'html'
    msg.send(fail_silently=True)
