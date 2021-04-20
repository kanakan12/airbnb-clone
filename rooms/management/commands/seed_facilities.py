from django.core.management.base import BaseCommand
from rooms.models import Facilty

class Command(BaseCommand):

    help = "This command creates faciliteis"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym"
        ]
        for f in facilities:
            Facilty.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))