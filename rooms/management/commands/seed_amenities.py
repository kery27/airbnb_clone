from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This command tells me that he loves me"

    ###"""def add_arguments self, parser:
    ###    parser.add_argument
    ###        "--times",
    ###        help="How many times do you want me to tell you that I love you? .",
    ###    """"

    def handle(self, *args, **options):
        ameinites = [
            "Air conditioning",
            "Alarm",
            "Balcony",
            "Bathroom",
            "Bed Linen",
        ]
        for a in ameinites:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created"))
