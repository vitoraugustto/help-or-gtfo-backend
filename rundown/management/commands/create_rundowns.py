import os
from rundown.models import Rundown, Expedition
from django.core.management.base import BaseCommand

rundowns = [
    {
        "title": "Deviation",
        "number": 1,
        "release_date": "2020-10-20",
        "expeditions": [
            {"title": "The Admin", "tier": "A", "difficulty": "1"},
            {"title": "Pid Search", "tier": "B", "difficulty": "1"},
            {"title": "The Officer", "tier": "B", "difficulty": "2"},
            {"title": "Reconnect", "tier": "C", "difficulty": "1"},
            {"title": "Decode", "tier": "C", "difficulty": "2"},
            {"title": "Deeper", "tier": "D", "difficulty": "1"},
        ],
    },
    {
        "title": "Infection",
        "number": 2,
        "release_date": "2022-12-07",
        "expeditions": [
            {"title": "The Dig", "tier": "A", "difficulty": "1"},
            {"title": "Sacrifice", "tier": "B", "difficulty": "1"},
            {"title": "Power Corrupts", "tier": "B", "difficulty": "2"},
            {"title": "Pathfinder", "tier": "B", "difficulty": "3"},
            {"title": "Septic", "tier": "B", "difficulty": "4"},
            {"title": "Triangulation", "tier": "C", "difficulty": "1"},
            {"title": "???", "tier": "C", "difficulty": "2"},
            {"title": "Statistics", "tier": "D", "difficulty": "1"},
            {"title": "Powerless", "tier": "D", "difficulty": "2"},
            {"title": "Crib", "tier": "E", "difficulty": "1"},
        ],
    },
    {
        "title": "The Vessel",
        "number": 3,
        "release_date": "2023-03-02",
        "expeditions": [
            {"title": "Resuscitation", "tier": "A", "difficulty": "1"},
            {"title": "Purification", "tier": "A", "difficulty": "2"},
            {"title": "Bolt", "tier": "A", "difficulty": "3"},
            {"title": "Thresold", "tier": "B", "difficulty": "1"},
            {"title": "Pressure", "tier": "B", "difficulty": "2"},
            {"title": "Alpha", "tier": "C", "difficulty": "1"},
            {"title": "Bianhua", "tier": "D", "difficulty": "1"},
        ],
    },
    {
        "title": "Contact",
        "number": 4,
        "release_date": "2023-04-27",
        "expeditions": [
            {"title": "Cytology", "tier": "A", "difficulty": "1"},
            {"title": "Foster", "tier": "A", "difficulty": "2"},
            {"title": "Onwards", "tier": "A", "difficulty": "3"},
            {"title": "Malachite", "tier": "B", "difficulty": "1"},
            {"title": "Variscite", "tier": "B", "difficulty": "2"},
            {"title": "Chrysolite", "tier": "B", "difficulty": "3"},
            {"title": "Cognition", "tier": "C", "difficulty": "1"},
            {"title": "Pabulum", "tier": "C", "difficulty": "2"},
            {"title": "Cuernos", "tier": "C", "difficulty": "3"},
            {"title": "Nucleus", "tier": "D", "difficulty": "1"},
            {"title": "Growth", "tier": "D", "difficulty": "2"},
            {"title": "Downwards", "tier": "E", "difficulty": "1"},
        ],
    },
    {
        "title": "Rebirth",
        "number": 5,
        "release_date": "2023-06-15",
        "expeditions": [
            {"title": "Floodways", "tier": "A", "difficulty": "1"},
            {"title": "Recollect", "tier": "A", "difficulty": "2"},
            {"title": "Mining", "tier": "A", "difficulty": "3"},
            {"title": "Smother", "tier": "B", "difficulty": "1"},
            {"title": "Discharge", "tier": "B", "difficulty": "2"},
            {"title": "Unseal", "tier": "B", "difficulty": "3"},
            {"title": "Diversion", "tier": "B", "difficulty": "4"},
            {"title": "Binary", "tier": "C", "difficulty": "1"},
            {"title": "Access", "tier": "C", "difficulty": "2"},
            {"title": "Starvation", "tier": "C", "difficulty": "3"},
            {"title": "Even Deeper", "tier": "D", "difficulty": "1"},
            {"title": "Error", "tier": "D", "difficulty": "2"},
            {"title": "KDS Deep", "tier": "E", "difficulty": "1"},
        ],
    },
]


class Command(BaseCommand):
    help = "Create the existing rundowns in the base game"

    def handle(self, *args, **options):
        for rundown in rundowns:
            if not Rundown.objects.filter(number=rundown["number"]).exists():
                created_rundown = Rundown.objects.create(
                    title=rundown["title"],
                    number=rundown["number"],
                    release_date=rundown["release_date"],
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Rundown {rundown["title"]} (R{rundown["number"]}) created successfully'
                    )
                )

                for expedition in rundown["expeditions"]:
                    if not Expedition.objects.filter(
                        title=expedition["title"],
                        tier=expedition["tier"],
                        difficulty=expedition["difficulty"],
                    ).exists():
                        Expedition.objects.create(
                            title=expedition["title"],
                            tier=expedition["tier"],
                            difficulty=expedition["difficulty"],
                            rundown=created_rundown,
                        )

                        self.stdout.write(
                            self.style.SUCCESS(
                                f'Expedition {expedition["title"]} (R{rundown["number"]}{expedition["tier"]}{expedition["difficulty"]}) created successfully'
                            )
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(
                                f'Expedition {expedition["title"]} (R{rundown["number"]}{expedition["tier"]}{expedition["difficulty"]}) already exists'
                            )
                        )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Rundown {rundown["title"]} (R{rundown["number"]}) already exists'
                    )
                )
