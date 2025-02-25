from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATES = [
        ('todo', 'Pendiente'),
        ('doing', 'En progreso'),
        ('done', 'Completada')
    ]

    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField()
    state = models.CharField()
    state = models.CharField(max_length=20, choices=STATES, default='todo')
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo
