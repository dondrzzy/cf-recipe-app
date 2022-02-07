from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Recipe                                #to access Book model        

# Create your views here.


def home(request):
   return render(request, 'recipe/recipes_home.html')


# Create your views here.
class RecipeListView(ListView):           #class-based view
   model = Recipe                         #specify model
   template_name = 'recipe/list.html'    #specify template 


class RecipeDetailView(DetailView):                       #class-based view
   model = Recipe                                        #specify model
   template_name = 'recipe/detail.html'                 #specify template
