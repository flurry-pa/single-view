import csv
from django.core.management.base import BaseCommand
from django.db.models import Q
from django.db.transaction import atomic

from sv.models import MusicWork, Author


class Command(BaseCommand):
    help = 'Imports music works from csv format'

    def add_arguments(self, parser):
        parser.add_argument(
            'import_path',
            help='Import path',
            type=str
        )

    @staticmethod
    def get_music_work(iswc, title):
        music_work = MusicWork.objects.filter(Q(iswc=iswc) | Q(title=title)).first()

        if music_work:
            update_fields = {}

            if iswc:
                update_fields['iswc'] = iswc
            if title:
                update_fields['title'] = title

            MusicWork.objects.filter(pk=music_work.pk).update(**update_fields)
        else:
            music_work = MusicWork.objects.create(title=title, iswc=iswc)

        return music_work

    @atomic
    def handle(self, *args, **options):
        import_path = options['import_path']

        with open(import_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                author_names_list = row['contributors'].split('|')
                title = row['title']
                iswc = row['iswc']

                music_work = self.get_music_work(title=title, iswc=iswc)

                for author_name in author_names_list:
                    author, _ = Author.objects.get_or_create(name=author_name)
                    music_work.authors.add(author)
