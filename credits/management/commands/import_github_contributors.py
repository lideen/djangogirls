from django.core.management.base import BaseCommand, CommandError

from credits.models import Contributor


class Command(BaseCommand):
    help = 'Imports contributors and credits from github.com'

    def add_arguments(self, parser):
        parser.add_argument('repo', type=str)

    def handle(self, *args, **options):
        repo = options.get('repo', None)
        self.stdout.write(self.style.SUCCESS('Importing contributors from "%s"' % repo))
        Contributor.import_from_github(repo=repo)
