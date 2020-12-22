from django.core.management.base import BaseCommand, CommandError
from main.models import Slidedeck, genSlideImages

class Command(BaseCommand):
    args = '<slide_id, slide_id, ...>'
    help = 'Generates slide images for the given slide models'

    def handle(self, *args, **options):
        operate = False
        if len(args) == 0:
            decks = Slidedeck.objects.all()
        else:
            decks = Slidedeck.objects.filter(pk__in = args)
            operate = True
            
        print('Number of Slidedecks: ', decks.count(), file=self.stdout)
        for slidedeck in decks:
            print('  ', slidedeck, file=self.stdout)

        if not operate:
            print('Specify which sliddeck you want (by pk) to generate slide images.', file=self.stdout)
            return

        for deck in decks:
            genSlideImages(deck)
