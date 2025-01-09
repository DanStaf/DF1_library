from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(email='danstaf@mail.ru'):

            user = User.objects.create(
                email='danstaf@mail.ru',
                first_name='Admin',
                last_name='Admin',
                is_staff=True,
                is_superuser=True,
                is_manager=True
            )

            user.set_password('admin')
            user.save()

        if not User.objects.filter(email='danstaf1@mail.ru'):
            user = User.objects.create(
                email='danstaf1@mail.ru',
                first_name='Reader',
                last_name='Reader',
                is_staff=False,
                is_superuser=False
            )

            user.set_password('12345')
            user.save()

        if not User.objects.filter(email='danstaf2@mail.ru'):
            user = User.objects.create(
                email='danstaf2@mail.ru',
                first_name='Manager',
                last_name='Manager',
                is_staff=False,
                is_superuser=False,
                is_manager=True
            )

            user.set_password('12345')
            user.save()

        print("Users created (if needed)")
