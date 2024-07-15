from django.contrib import admin

from .models.client import Client
from .models.package import Package, packageName, packageDescription

admin.site.register(Client)
admin.site.register(Package)
admin.site.register(packageName)
admin.site.register(packageDescription)