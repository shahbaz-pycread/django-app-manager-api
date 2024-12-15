from django.contrib import admin
from .models import App

admin.site.register(App)

admin.site.site_header = 'App Manager Admin'
