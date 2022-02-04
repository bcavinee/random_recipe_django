from bs4 import BeautifulSoup
import requests
import random
import unicodedata

url= 'https://mealpreponfleek.com/35-macro-friendly-meal-prep-recipes/'
result= requests.get(url)

doc= BeautifulSoup(result.text,'html.parser')



#Collecting the name of the dishes, then adding them to a list.  The blank spaces are being stripped.
recipe_name_h3 = doc.find_all("h3")

recipe_name_list_untruncated= []

for h3_tag in recipe_name_h3:

	try:	
		recipe_name_list_untruncated.append(h3_tag.a.text)
	except AttributeError as e:
		pass

recipe_list= [recipe_name_list_untruncated[x] for x in range(37)]
recipe_name= [recipe for recipe in recipe_list if recipe != '']

#Collecting the macros from recipes and adding to a list.
macronutrients= doc.find_all('p')
macronutrients_list_untruncated= [macro.text for macro in macronutrients]
macronutrients_list = [macronutrients_list_untruncated[x] for x in range(14,89)]
	
macronutrients_list_check= [x for x in macronutrients_list if x != '']
macronutrients_list= [x.replace("\xa0","") for x in macronutrients_list_check]
macronutrients= [x for x in macronutrients_list if x != ""]
del macronutrients[0]

#Replaced ',' with '|'
macronutrients[28]= macronutrients[28].replace(',', ' |')

#Collecting the URL to the dish. 

url_find= doc.find_all('h3')
url_list= []
for h3 in url_find:
	for link in h3.find_all('a'):
		urls=link.get('href')
		url_list.append(urls)


#removing duplicates

for x in range(len(url_list)):
	try:
		url_one= url_list[x]
		url_two= url_list[x +1]
		if url_one == url_two:
			url_list.remove(url_one)

	except IndexError as e:
		e		


url= [url_list[x] for x in range(0,35)]


#Making a skeleton dictonary to add recipe values to

recipe_data= []

for x in range(1,36):


	dictonary= {f"Recipe {x}": '','Fat': '','Calories': '', 'Carbohydrates' : '', 'Protein' : '',f'Link {x}' : ''}

	recipe_data.append(dictonary)


for x in macronutrients:
	print(x)

#Looping through recipe data and adding it to recipe_data dictonary



#protein,carbs,fat,calories= macronutrients[0].split('|')

for x in range(35):
	
	protein,carbs,fat,calories= macronutrients[x].split('|')
	

	recipe_data[x][f'Recipe {x+1}']= recipe_name[x]
	recipe_data[x][f'Calories']= calories
	recipe_data[x][f'Fat']= fat
	recipe_data[x][f'Carbohydrates']= carbs
	recipe_data[x][f'Protein']= protein
	recipe_data[x][f'Link {x+1}'] = url[x]