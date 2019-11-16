import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from reservations import models as resvervation_models
from users import models as user_models
from rooms import models as room_models

NAME = "reservations"


class Command(BaseCommand):
    help = "This command tells me that he loves me"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many list do you want to create",
        )

    # seed에 나온 메뉴얼대로 씀
    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        # 임의로 생성하려는 엔티티를 정해
        seeder.add_entity(
            resvervation_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(users),
                # many-to-many 에서는 얘를 뺀다
                # 여긴 포린키여서 추가
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created"))
