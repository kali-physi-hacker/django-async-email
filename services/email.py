from django.core.mail import send_mail

import django_rq


def sender():
    """
    Send a test email
    """
    subject = "Finally Done"
    message = "Currently, Python anwhere does not support asynchronous tasks using thread. This is a test to send email asynchronously your RQ"
    email_from = "info@test.com"
    recipient_list = ["desmond@gradia.net", "browndesmond30@yahoo.com"]

    for _ in range(5):
        send_mail(subject=subject, message=message, from_email=email_from, recipient_list=recipient_list)


def send():
    django_rq.enqueue(sender)
