from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=255, verbose_name='nombre')

    class Meta:
        verbose_name = 'Familia'


    def __str__(self):
        return self.name


class Task(models.Model):
    STATES = [
        ('todo', 'Pendiente'),
        ('doing', 'En progreso'),
        ('done', 'Completada')
    ]

    family = models.ForeignKey(
        Family, 
        on_delete=models.CASCADE, 
        related_name="tasks",
        verbose_name='familia'
    )
    title = models.CharField(max_length=255, verbose_name='título')
    description = models.TextField(verbose_name='descripción')
    state = models.CharField(
        max_length=20, 
        choices=STATES, 
        default='todo',
        verbose_name='estado'
    )
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    due_date = models.DateField(null=True, blank=True, verbose_name='Fecha de vencimiento')

    class Meta: 
        verbose_name = 'Tarea'

    def __str__(self):
        return self.title
