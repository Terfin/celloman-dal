from django.contrib import admin
from .models import Client, ClientType
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'view_minutes_price', 'view_sms_price']

    def view_minutes_price(self, obj):
        return '${}'.format(obj.minutes_price)

    def view_sms_price(self, obj):
        return '${}'.format(obj.sms_price)