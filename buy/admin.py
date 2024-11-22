from django.contrib import admin

from .models import CategoryModel, HouseModel

admin.site.register([CategoryModel, HouseModel])