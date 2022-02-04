from bs4 import BeautifulSoup
import requests
import random
import unicodedata


result= requests.get(url)

doc= BeautifulSoup(result.text,'html.parser')

#Getting the names of the recipes from the H2 tag.  Looping through them and adding the text to a list
recipe_name_h2 = doc.find_all("h2")
recipe_names= [h2.text for h2 in recipe_name_h2]


#Collecting all of the divs with the class "shadebox".  Then loooping through them and getting all the text of all the paragraph tags and adding them to a list

macronutrients_div= doc.find_all("div", {"class" : "shadebox"})
macronutrients_untruncated= []
for div in macronutrients_div:
	for p in div.find_all('p'):
		macronutrients_untruncated.append(p.text)


#Added the caloires and the macronutrients together since they were sepearte in the list
macronutrients_withgrams= []

y=0
z=0
for x in range(len(macronutrients_untruncated)):
	try:
		macronutrients_withgrams.append(macronutrients_untruncated[x+z] + "\n" +  macronutrients_untruncated[y+1+z])
		y += 1
		z+= 1
	except IndexError as e:
		e

#Getting rid of the g/n in the list

macronutrients= [x.replace("g\n","") for x in macronutrients_withgrams]
macronutrients= [x.replace("\n"," ") for x in macronutrients]

#Getting all of the urls from the <a> tag within the paragraph tag
url_find= doc.find_all('p')
url_list_untruncated= []
for p in url_find:
	for link in p.find_all('a'):
		urls=link.get('href')
		url_list_untruncated.append(urls)

url_list_with_dupo= [url_list_untruncated[x] for x in range(6,33)]


#Added a specfic recipe since the url was not givin in the page.  Also added a recipe that did not contain a dupo to make the next loop easier
url_list_with_dupo.insert(11,'https://gimmedelicious.com/chipotles-chicken-burrito-bowl-with-cilantro-lime-rice/')
url_list_with_dupo.insert(12,'https://gimmedelicious.com/chipotles-chicken-burrito-bowl-with-cilantro-lime-rice/')
url_list_with_dupo.insert(7,'https://healthyeater.com/turkey-burger-recipe')

#Looping through urls with dupos and adding only one to a list

urls= [url_list_with_dupo[x] for x in range(0,30,2)]


#Making an empty dictonary
recipe_data=[]
for x in range(1,16):


	dictonary= {f"Recipe {x}": '','Fat': '','Calories': '', 'Carbohydrates' : '', 'Protein' : '',f'Link {x}' : ''}

	recipe_data.append(dictonary)




#Due to some items in the list not having a fiber amount, when running the for loop to split the macronutrients into individual variables, it gave a flag.  Added fiber to items without fiber.
macronutrients[7]= macronutrients[7] + 'Fiber: 0 '
macronutrients[9]= macronutrients[9] + 'Fiber: 0 '


#Looping through macronutrient list, splitting the individual calories/macros into individual variables.  Then using a try, except clause to convert str --> int and str-->float-->int.  Then adding to dict

for x in range(15):


	space,calories,space_two,protein,space_three,carbs,space_four,fat,space_five,fiber,space_six= macronutrients[x].split(' ')


	try:
		int_calories= int(calories)
		int_protein= int(protein)
		int_carbs= int(carbs)
		int_fat= int(fat)
	except ValueError as e:
		int_calories= int(float(calories))
		int_protein= int(float(protein))
		int_carbs= int(float(carbs))
		int_fat= int(float(fat))		

	
	recipe_data[x][f'Recipe {x+1}']= recipe_names[x]
	recipe_data[x]['Calories']= int_calories
	recipe_data[x]['Fat']= int_fat
	recipe_data[x]['Carbohydrates']= int_carbs
	recipe_data[x]['Protein']= int_protein
	recipe_data[x][f'Link {x+1}'] = urls[x]



