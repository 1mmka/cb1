from django.shortcuts import render
from django.views.generic import CreateView,ListView
from cream.forms import larekForm,creamForm
from django.urls import reverse_lazy
from cream.models import Larek,IceCream

# Create your views here.
def home(request):
    return render(request,'home.html')

class createLarek(CreateView):
    form_class = larekForm
    template_name = 'larek.html'
    success_url = reverse_lazy('home-page')
    
class createCream(CreateView):
    form_class = creamForm
    template_name = 'ice.html'
    success_url = reverse_lazy('home-page')