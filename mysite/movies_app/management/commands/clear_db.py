from django.core.management.base import BaseCommand, CommandError
from movies_app.models import Person, Movie

class Command(BaseCommand):
    help = 'Deletes all Movies & Persons from database'

    def handle(self, *args, **options):
        Movie.objects.all().delete()
        Person.objects.all().delete()