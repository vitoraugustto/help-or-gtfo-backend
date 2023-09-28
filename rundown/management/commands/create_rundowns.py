import os
from rundown.models import Rundown, Expedition
from django.core.management.base import BaseCommand

rundowns = [
    {
        "title": "Deviation",
        "number": 1,
        "release_date": "2020-10-20",
        "expeditions": [
            {"title": "The Admin", "tier": "A", "difficulty": "1", "sectors": ["Main"]},
            {
                "title": "Pid Search",
                "tier": "B",
                "difficulty": "1",
                "sectors": ["Main"],
            },
            {
                "title": "The Officer",
                "tier": "B",
                "difficulty": "2",
                "sectors": ["Main"],
            },
            {"title": "Reconnect", "tier": "C", "difficulty": "1", "sectors": ["Main"]},
            {"title": "Decode", "tier": "C", "difficulty": "2", "sectors": ["Main"]},
            {"title": "Deeper", "tier": "D", "difficulty": "1", "sectors": ["Main"]},
        ],
    },
    {
        "title": "Infection",
        "number": 2,
        "release_date": "2022-12-07",
        "expeditions": [
            {"title": "The Dig", "tier": "A", "difficulty": "1", "sectors": ["Main"]},
            {"title": "Sacrifice", "tier": "B", "difficulty": "1", "sectors": ["Main"]},
            {
                "title": "Power Corrupts",
                "tier": "B",
                "difficulty": "2",
                "sectors": ["Main"],
            },
            {
                "title": "Pathfinder",
                "tier": "B",
                "difficulty": "3",
                "sectors": ["Main"],
            },
            {"title": "Septic", "tier": "B", "difficulty": "4", "sectors": ["Main"]},
            {
                "title": "Triangulation",
                "tier": "C",
                "difficulty": "1",
                "sectors": ["Main"],
            },
            {"title": "???", "tier": "C", "difficulty": "2", "sectors": ["Main"]},
            {
                "title": "Statistics",
                "tier": "D",
                "difficulty": "1",
                "sectors": ["Main"],
            },
            {"title": "Powerless", "tier": "D", "difficulty": "2", "sectors": ["Main"]},
            {"title": "Crib", "tier": "E", "difficulty": "1", "sectors": ["Main"]},
        ],
    },
    {
        "title": "The Vessel",
        "number": 3,
        "release_date": "2023-03-02",
        "expeditions": [
            {
                "title": "Resuscitation",
                "tier": "A",
                "difficulty": "1",
                "sectors": ["Main"],
            },
            {
                "title": "Purification",
                "tier": "A",
                "difficulty": "2",
                "sectors": ["Main"],
            },
            {"title": "Bolt", "tier": "A", "difficulty": "3", "sectors": ["Main"]},
            {"title": "Thresold", "tier": "B", "difficulty": "1", "sectors": ["Main"]},
            {"title": "Pressure", "tier": "B", "difficulty": "2", "sectors": ["Main"]},
            {"title": "Alpha", "tier": "C", "difficulty": "1", "sectors": ["Main"]},
            {"title": "Bianhua", "tier": "D", "difficulty": "1", "sectors": ["Main"]},
        ],
    },
    {
        "title": "Contact",
        "number": 4,
        "release_date": "2023-04-27",
        "expeditions": [
            {
                "title": "Cytology",
                "tier": "A",
                "difficulty": "1",
                "sectors": ["Main", "Secondary"],
            },
            {
                "title": "Foster",
                "tier": "A",
                "difficulty": "2",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Onwards",
                "tier": "A",
                "difficulty": "3",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Malachite",
                "tier": "B",
                "difficulty": "1",
                "sectors": ["Main", "Secondary"],
            },
            {
                "title": "Variscite",
                "tier": "B",
                "difficulty": "2",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Chrysolite",
                "tier": "B",
                "difficulty": "3",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Cognition",
                "tier": "C",
                "difficulty": "1",
                "sectors": ["Main", "Secondary"],
            },
            {
                "title": "Pabulum",
                "tier": "C",
                "difficulty": "2",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Cuernos",
                "tier": "C",
                "difficulty": "3",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Nucleus",
                "tier": "D",
                "difficulty": "1",
                "sectors": ["Main", "Secondary"],
            },
            {
                "title": "Growth",
                "tier": "D",
                "difficulty": "2",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Downwards",
                "tier": "E",
                "difficulty": "1",
                "sectors": ["Main", "Secondary"],
            },
        ],
    },
    {
        "title": "Rebirth",
        "number": 5,
        "release_date": "2023-06-15",
        "expeditions": [
            {
                "title": "Floodways",
                "tier": "A",
                "difficulty": "1",
                "sectors": ["Main", "Secondary"],
            },
            {
                "title": "Recollect",
                "tier": "A",
                "difficulty": "2",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Mining",
                "tier": "A",
                "difficulty": "3",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Smother",
                "tier": "B",
                "difficulty": "1",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Discharge",
                "tier": "B",
                "difficulty": "2",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Unseal",
                "tier": "B",
                "difficulty": "3",
                "sectors": ["Main", "Secondary"],
            },
            {"title": "Diversion", "tier": "B", "difficulty": "4", "sectors": ["Main"]},
            {
                "title": "Binary",
                "tier": "C",
                "difficulty": "1",
                "sectors": ["Main", "Secondary"],
            },
            {
                "title": "Access",
                "tier": "C",
                "difficulty": "2",
                "sectors": ["Main", "Secondary", "Overload"],
            },
            {
                "title": "Starvation",
                "tier": "C",
                "difficulty": "3",
                "sectors": ["Main", "Secondary"],
            },
            {
                "title": "Even Deeper",
                "tier": "D",
                "difficulty": "1",
                "sectors": ["Main", "Secondary"],
            },
            {"title": "Error", "tier": "D", "difficulty": "2", "sectors": ["Main"]},
            {"title": "KDS Deep", "tier": "E", "difficulty": "1", "sectors": ["Main"]},
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
                            main_sector=True
                            if "Main" in expedition["sectors"]
                            else False,
                            secondary_sector=True
                            if "Secondary" in expedition["sectors"]
                            else False,
                            overload_sector=True
                            if "Overload" in expedition["sectors"]
                            else False,
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
