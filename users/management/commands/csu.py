import os

from django.core.management import BaseCommand

from users.models import User
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="kill2002@mail.ru",
            first_name="Кирилл",
            last_name="Серебряков",
            is_staff=True,
            is_superuser=True
        )

        user.set_password(os.getenv('SUPASSWORD'))
        user.save()