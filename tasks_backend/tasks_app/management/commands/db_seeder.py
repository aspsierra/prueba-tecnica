from django.core.management.base import BaseCommand
from tasks_app.models import Family, Task
from faker import Faker
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        fake = Faker('es_ES')

        families = [Family(name=fake.job()) for _ in range(10)]
        Family.objects.bulk_create(families)
        families = Family.objects.all()

        states = ['todo', 'doing', 'done']

        for _ in range(50):
            Task.objects.create(
                family=random.choice(families),
                title=fake.sentence(),
                description=fake.paragraph(),
                state=random.choice(states),
                due_date=fake.date_between(start_date='today', end_date="+30d")
            )

        self.stdout.write(self.style.SUCCESS("Base de datos poblada con exito"))



        
    