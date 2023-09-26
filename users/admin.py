from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    readonly_file = ('id',)


admin.site.register(Profile, ProfileAdmin)
