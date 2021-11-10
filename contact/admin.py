from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    fields = ('full_name', 'email', 'subject', 'message')
    list_display = ('full_name', 'email', 'subject', 'message')


admin.site.register(Contact, ContactAdmin)
