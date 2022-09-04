from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(blog)
admin.site.site_title = 'Django Admin Panel Customization'
admin.site.site_header ='Django Admin Panel Customization'