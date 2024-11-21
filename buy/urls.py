from django.urls import path

from .views import HomeView, DetailView, PropertiesView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('', ContactView.as_view(), name='contact_page'),
    path('', DetailView.as_view(), name='detail_page'),
    path('', PropertiesView.as_view(), name='properties_page'),
]
