from django.contrib import admin

from .models import Client, Package, packageName, packageDescription

admin.site.register(Client)
admin.site.register(Package)
admin.site.register(packageName)
admin.site.register(packageDescription)