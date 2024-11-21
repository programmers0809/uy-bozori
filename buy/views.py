from django.shortcuts import render

from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
    
class PropertiesView(View):
    def get(self, request):
        return render(request, 'properties.html')
    
class DetailView(View):
    def get(self, request):
        return render(request, 'detail.html')