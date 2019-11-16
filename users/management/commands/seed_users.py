from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = "This command tells me that he loves me"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many users do you want to create",
        )

    # seed에 나온 메뉴얼대로 씀
    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        # 상속받은 유저에서 저기능을 빼고 싶은경우
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Users created"))
