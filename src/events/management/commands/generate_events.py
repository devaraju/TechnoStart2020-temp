from django.core.management.base import BaseCommand, CommandError


from events.models import Event

import os
import json

class Command(BaseCommand):

    # def add_arguments(self, parser):
    #     parser.add_argument('events_file', type=str, help="JSON file that contains events data")

    def handle(self, *args, **kwargs):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        # events_file = kwargs["events.json"]
        events_file = os.path.join(base_dir, 'events.json')

        # >>> EVENTS DATA <<<
        with open(f"{events_file}") as file:
            data = json.load(file)

            for row in data:
                title = row["title"]
                description = row["description"]
                category = row["category"]
                no_of_participants = row["no_of_participants"]
                try:
                    event = Event.objects.get(title=title)
                    self.stdout.write(self.style.ERROR(f'Event:"{title}" Already existed.'))

                except:
                    event = Event.objects.create(
                        title=title,
                        description=description,
                        category=category,
                        no_of_participants=no_of_participants,
                    )
                    self.stdout.write(self.style.SUCCESS(f'successfully added {title}'))
                # except:
                #     self.stdout.write(self.style.ERROR(f'Error occured with event:"{title}"'))
