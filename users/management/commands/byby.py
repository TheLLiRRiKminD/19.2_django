from django.core.mail import send_mail
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_mail(
            'Test Subject',
            'Test message body',
            'ya.kill2002@yandex.ru',
            ['kilol9436@gmail.com'],
            fail_silently=False,
        )
