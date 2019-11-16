import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models

NAME = "lists"


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
            list_models.List,
            number,
            {
                "user": lambda x: random.choice(users),
                # many-to-many 에서는 얘를 뺀다
                # "rooms": lambda x: random.choice(rooms),
            },
        )

        # 리스트는 룸과 다대다관계로
        # 임의로 생성한 리스트에 임의로 골라낸 룸을 연결 해줘야해
        # 시드로 생성한 리스트목록을 돌면서
        # 리스트 키값들 가지고 있고
        # 전체로 생성한 룸중에서 임의로 숫자를 만들고 그숫자가 짝수일때만 리스트에 추가함
        # 임의개의 룸을 생성한 리스트를 완성한다.
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            # *to_add를 해서 어레이안의 변수를 추가한다.
            # 걍하면 어레이주소가 넘어감
            list_model.rooms.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created"))
