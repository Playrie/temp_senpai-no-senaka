from django.contrib import admin

# Register your models here.
from .models import RestRequest,Schedule

class RestRequestAdmin(admin.ModelAdmin):

    list_display = ('kerbero_id', 'head_name', 'start_date')


class ScheduleAdmin(admin.ModelAdmin):

    list_display = ('kerbero_id', 'date')


admin.site.register(RestRequest, RestRequestAdmin)
admin.site.register(Schedule, ScheduleAdmin)
