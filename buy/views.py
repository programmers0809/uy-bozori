from django.shortcuts import render

from django.views import View

from .models import CategoryModel

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
    
class PropertiesView(View):
    def get(self, request):
        
        category_list = CategoryModel.objects.all()
    
    
        context = {
        'category_list': category_list,
    }
        return render(request, 'properties.html', context=context)
    


class DetailView(View):
    def get(self, request):
        return render(request, 'detail.html',  )