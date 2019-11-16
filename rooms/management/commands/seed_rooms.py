import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


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
    # 랜덤 모듈 임포트후 임의변수 생성하고 임의 룸을 생성시킴
    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        # 데이터가 큰경우 쓰지 않아 페이징 처리 해야해
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        # 상속받은 유저에서 저기능을 빼고 싶은경우
        seeder.add_entity(
            room_models.Room,
            number,
            {  # 페이크 주소를 만들어 낸다
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(0, 300),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": lambda x: random.randint(0, 5),
                "baths": lambda x: random.randint(0, 5),
                "guest": lambda x: random.randint(0, 5),
            },
        )
        # 임의로 만든 방은 키를 리턴한다
        # 이걸 다듬어서 가지고 있다가 늘어 뜨린다.
        # 임의로 만든 방의 키를 받아와서 포토를 생성할때 포린키로 너준다
        # 포토의 갯수는 3에서 10~17개 사이
        # 포토의 파일은 파일 주소를 말하는데 룸포토스 안에
        create_photos = seeder.execute()
        cleated_clean = flatten(list(create_photos.values()))

        # 어메니티, 패실리티도 매니키로 묶여서 달리 작업해야될듯
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in cleated_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created"))
