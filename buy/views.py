from django.shortcuts import render

from django.views import View

from .models import CategoryModel, HouseModel,CarouselItem,Contact,Contoct
from django.shortcuts import render, redirect

from .forms import ContactForm

def home(request):
    carousel_items = CarouselItem.objects.all()  # Karusel uchun elementlar
    all_house_list = HouseModel.objects.all()  # Uylar ro'yxati
    contact_info = Contact.objects.first()  # Birinchi kontakt ma'lumotlarini olish
    contoct_info = Contoct.objects.first()  # Birinchi contoct ma'lumotlarini olish

    # Kontakt formasi bilan ishlash
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Forma ma'lumotlarini saqlash
            return redirect('home')  # Forma yuborilgandan keyin sahifani yangilash
    else:
        form = ContactForm()  # Bo‘sh forma yaratish

    # Shablonga ma'lumotlarni jo‘natish
    return render(request, 'home.html', {
        'contact_info': contact_info,  # Kontakt ma'lumotlari
        'carousel_items': carousel_items,  # Karusel elementlari
        'all_house_list': all_house_list,  # Uylar ro'yxati
        'form': form,  # Kontakt shakli
        'contoct_info': contoct_info  # Contoct ma'lumotlari
    })


 
class ContactView(View):
    def get(self, request):
        # Retrieve contact information from the ContactInfo model
        contact_info = Contact.objects.first()  # Or use other queryset filters as needed

        # Initialize an empty form
        form = ContactForm()

        # Render the contact page with the form and contact_info context
        return render(request, 'contact.html', {
            'form': form,
            'contact_info': contact_info  # Pass the contact information to the template
        })

    def post(self, request):
        # Retrieve contact information for post requests
        contact_info = ContactInfo.objects.first()  # Or filter if you need specific info

        # Initialize the form with POST data
        form = ContactForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save form data (for example, saving to a Contact model)
            form.save()

            # Redirect to a success page (or the same page)
            return redirect('contact')  # Redirect to contact page or any other desired page

        # If the form is not valid, re-render the form with the error messages
        return render(request, 'contact.html', {
            'form': form,
            'contact_info': contact_info  # Pass the contact information again
        })

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