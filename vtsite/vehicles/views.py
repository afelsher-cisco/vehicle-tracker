from django.shortcuts import render
from django.template.context import RequestContext
from .forms import NameForm

def index(request):
    return render(request, 'vehicles/home.html', {})

def test(request, number):
    return render(request, 'vehicles/test.html', {'number': number})

def checkin(request):
   # if this is a POST request we need to process the form data
   if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = NameForm(request.POST)
      # check whether it's valid:
      if form.is_valid():
         # process the data in form.cleaned_data as required
         # ...
         # redirect to a new URL:
         return HttpResponseRedirect('/thanks/')
   # if a GET (or any other method) we'll create a blank form
   else:
        form = NameForm()
   return render(request, 'vehicles/checkin.html', {'form':form})
   #return render(request, 'vehicles/checkin.html', {})

def checkout(request):
    return render(request, 'vehicles/checkout.html', {})
