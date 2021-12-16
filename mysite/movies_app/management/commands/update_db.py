from django.core.management.base import BaseCommand, CommandError
from movies_app.services import update_db


class Command(BaseCommand):
    help = "Retrieves Movies & Peoples from API"

    def handle(self, *args, **options):
        update_db()
