from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'date', 'venue', 'host'
    ]
    list_filter = ('name', 'date', 'host', 'venue')

admin.site.register(Event, EventAdmin)
