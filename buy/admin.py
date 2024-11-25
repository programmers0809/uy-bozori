from django.contrib import admin

from .models import CategoryModel, HouseModel,CarouselItem,Contact

admin.site.register([CategoryModel, HouseModel,CarouselItem,Contact])

