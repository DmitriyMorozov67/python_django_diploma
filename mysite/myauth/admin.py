from django.contrib import admin
from .models import Profile, Avatar


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'fullName', 'user']
    list_display_links = ['pk', 'fullName']
    ordering = 'pk',


@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ['pk', '__str__']
    list_display_links = 'pk',
    ordering = 'pk',

