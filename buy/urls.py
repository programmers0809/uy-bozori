from django.urls import path

from .views import DetailView, PropertiesView, ContactView
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Map the home view to the root URL

    path('contact/', ContactView.as_view(), name='contact'),  # 'contact' nomi bilan URL aniqlangan
    path('detail/', DetailView.as_view(), name='detail_page'),
    path('properties/', PropertiesView.as_view(), name='properties_page'),
]
