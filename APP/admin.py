from django.contrib import admin
from .models import checkout

class WithdrawalNoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'mail', 'phone']
    ordering = ['id']  # Указываем поле для сортировки

admin.site.register(checkout, WithdrawalNoticeAdmin)