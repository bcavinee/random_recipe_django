from django.db import models



class recipes(models.Model):

	recipe_name= models.CharField(max_length=100)
	calories= models.IntegerField()
	protein= models.IntegerField()
	fat= models.IntegerField()
	carbs= models.IntegerField()
	link= models.CharField(max_length=100)





