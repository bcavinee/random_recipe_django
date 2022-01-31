from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import recipes
from django.shortcuts import render, redirect
import random
from .forms import macro_calorie_form, contact_form
from django.contrib import messages
from django.db.models import Q
def index(request):

           

 

    if request.method == 'POST':
        form= macro_calorie_form(request.POST)
        if form.is_valid():
            calories_min_user= form.cleaned_data['calories_min']
            calories_max_user= form.cleaned_data['calories_max']
            fat_min_user= form.cleaned_data['fat_min']
            fat_max_user= form.cleaned_data['fat_max']
            carbohydrates_min_user= form.cleaned_data['carbohydrates_min']
            carbohydrates_max_user= form.cleaned_data['carbohydrates_max']
            protein_min_user= form.cleaned_data['protein_min']
            protein_max_user= form.cleaned_data['protein_max']

            user_search= recipes.objects.filter(Q(calories__range=(calories_min_user,calories_max_user)) & Q(fat__range=(fat_min_user,fat_max_user)) & Q(carbs__range=(carbohydrates_min_user,carbohydrates_max_user)) & Q(protein__range=(protein_min_user,protein_max_user)))
            
            try:
                recipe=list(user_search)
                recipe_data= random.sample(recipe,1)
                link_value= []
                for link_name in recipe_data:
                    link_value.append(link_name.link)

                
                return redirect(link_value[0])

            except ValueError as e:
               
                messages.error(request, "Sorry, currently no recipes exist in our database with this specifc calorie/macronutrient combination.  Please try another combination.")
                form= macro_calorie_form()

    else:
        form=macro_calorie_form()

    
   
    return render(request,'recipes/recipe_frontpage.html', {'form': form})

def contact_us(request):

    if request.method=='POST':
        form_two= contact_form(request.POST)
        if form_two.is_valid():
            email= form.cleaned_data(['email'])
            subject= form.cleaned_data(['subject'])
            message= form.cleaned_data(['message'])

    return render(request,'contact_us.html', {'form_two': form_two})

def displayrecipe(request):

    recipe= list(recipes.objects.all())
    recipe_data= random.sample(recipe,1)
    link_value= []
    for link_name in recipe_data:
        link_value.append(link_name.link)

    return redirect(link_value[0])
