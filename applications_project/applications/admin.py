from applications.models import Type, Department, Record
from django.contrib import admin
from applications.actions import export_as_xls
from django import forms
from django.db import models

admin.site.register(Type)
admin.site.register(Department)


class RecordAdmin(admin.ModelAdmin):
    list_display = ['street', 'house', 'appartment', 'name', 'priority',
                    'request_date', 'type', 'subscriber_status', 'department',
                    'connection_date', 'status']
    list_filter = ['request_date', 'street', 'priority', 'type',
                   'subscriber_status', 'department', 'connection_date',
                   'status']
    search_fields = ['street']
    actions = [export_as_xls]
    date_hierarchy = 'request_date'
    formfield_overrides = {
        models.BigIntegerField: {'widget': forms.TextInput(
            attrs={'size': '40'})},
    }

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        try:
            extra_context['request_date_gte'] = request.GET['date__gte']
        except:
            pass
        try:
            extra_context['request_date_lte'] = request.GET['date__lte']
        except:
            pass

        if 'status__exact' in request.GET:
            q = request.GET.copy()
            q['status__exact'] = '0'
            request.GET = q
            request.META['QUERY_STRING'] = request.GET.urlencode()

        return super(RecordAdmin, self).changelist_view(request, extra_context)

admin.site.register(Record, RecordAdmin)
