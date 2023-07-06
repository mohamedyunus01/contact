from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import *


def contact_view(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("/thank you for your query/")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)



def viewDetails(request):
    obj = Contact.objects.get(email='yunus@gmail.com')
    context= {'i':obj}
    return render(request, 'details.html', context)

    