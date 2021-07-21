from django.core.management.base import BaseCommand

from services.email import send


class Command(BaseCommand):
    """
    Send a test email
    """
    def handle(self, *args, **options):
        send()
        self.stdout.write(self.style.SUCCESS("Email sent successfully"))