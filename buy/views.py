from django.shortcuts import render

from django.views import View

from .models import CategoryModel, HouseModel

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
    
class PropertiesView(View):
    def get(self, request):
        
        category_list = CategoryModel.objects.all()
        all_house_list = HouseModel.manager.all().order_by('-publish_time')
    
    
        context = {
        'category_list': category_list,
        'all_house_list': all_house_list,
    }
        return render(request, 'properties.html', context=context)
    


class DetailView(View):
    def get(self, request):
        return render(request, 'detail.html',  )