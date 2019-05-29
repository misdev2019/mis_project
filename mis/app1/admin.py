from django.contrib import admin
from .models import *

# Register your models here.
class UserInfo(admin.ModelAdmin):
    fieldsets = [
        ('user', {'fields': ['user']}),
        ('user_type', {'fields': ['user_type']})
    ]
    search_fields = ['user']
admin.site.register(userinfo, UserInfo)

class EmailVerifyRecordAdmin(admin.ModelAdmin):
    """
    list_display: 后台列出的字段
    search_fields: 搜索框及支持搜索的字段
    list_filter: 添加过滤器
    """
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
    
