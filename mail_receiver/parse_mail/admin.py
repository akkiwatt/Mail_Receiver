from __future__ import unicode_literals
from django.contrib import admin

#---Register you table for UI access
from .models import email_info
admin.site.register(email_info)

