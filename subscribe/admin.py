from django.contrib import admin
from .models import Subscribe

# Register your models here.


class SubscribeAdmin(admin.ModelAdmin):
    fields = ('full_name', 'email')
    list_display = ('full_name', 'email')


admin.site.register(Subscribe, SubscribeAdmin)
