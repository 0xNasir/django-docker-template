from django.contrib import admin

# Register your models here.
from sports.models import Sport, Event, Selection


class SportAdmin(admin.ModelAdmin):
    class Meta:
        model = Sport

    list_display = ['name', 'slug']


admin.site.register(Sport, SportAdmin)

admin.site.register(Event)
admin.site.register(Selection)
