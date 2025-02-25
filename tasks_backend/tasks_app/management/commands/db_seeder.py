from django.core.management.base import BaseCommand
from tasks_app.models import Family, Task
from lorem_text import lorem
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        families = ['Programación', 'RRHH', 'Otros']

        for type in families:
             Family.objects.get_or_create(name=type)
        
        states =  ['todo', 'doing', 'done']

        for i in range(10):
            Task.objects.create(
                family=Family.objects.order_by('?').first(),
                title=f'Tarea {i+1}',
                description=lorem.paragraph(),
                state=random.choice(states)
            )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))


        
    