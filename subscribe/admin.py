from django.contrib import admin
from .models import Subscribe

# Register your models here.


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name',)


admin.site.register(Subscribe, SubscribeAdmin)
