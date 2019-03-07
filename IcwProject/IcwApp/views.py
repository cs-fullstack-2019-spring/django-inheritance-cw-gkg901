from .forms import contactForm

from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.

# RENDERS INDEX PAGE
def index(request):
    return render(request, 'IcwApp/index.html')


# RENDERS ABOUT PAGE

def aboutus(request):
    return render(request, 'IcwApp/aboutus.html')


# RENDERS GALLERY PAGE

def gallery(request):
    return render(request, 'IcwApp/gallery.html')


# RENDERS RESOURCES PAGE
def resources(request):
    return render(request, 'IcwApp/resources.html')


# RENDERS CONTACT PAGE AND INJECTS FORM
def contactus(request):
    form = contactForm(request.POST or None)
    context = {
        'form': contactForm
    }
    if form.is_valid():
        form.save()
    return render(request, 'IcwApp/contactus.html', context)


# LISTS FORM OBJECTS
def secret(request):
    allForms = contactForm.objects.all()
    context = {
        'form': allForms
    }

    return render(request, 'IcwApp/secret.html', context)
