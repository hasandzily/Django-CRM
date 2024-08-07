from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'city', 'state', 'zipcode', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode')
    list_filter = ('created_at', 'city', 'state')

    class Meta:
        model = Record