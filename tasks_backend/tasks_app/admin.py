from django.contrib import admin
from .models import Family, Task


class FamilyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']

class TaskAdmin(admin.ModelAdmin):
    search_fields = ['title', 'family']
    list_display = ['title', 'family', 'state', 'due_date']
    list_filter = ['family', 'state']

admin.site.register(Task, TaskAdmin)
admin.site.register(Family, FamilyAdmin)