from django import forms
from crispy_forms.helper import FormHelper


class macro_calorie_form(forms.Form):

	calories_min= forms.IntegerField(label="calories_min",required=True, widget=forms.TextInput(attrs={'placeholder': 'Min'}))
	calories_max= forms.IntegerField(label="calories_max",required=True,widget=forms.TextInput(attrs={'placeholder': 'Max'}))
	fat_min= forms.IntegerField(label="fat_min",required=True,widget=forms.TextInput(attrs={'placeholder': 'Min'}))
	fat_max= forms.IntegerField(label="fat_max",required=True,widget=forms.TextInput(attrs={'placeholder': 'Max'}))
	carbohydrates_min= forms.IntegerField(label="carbohydrates_min",required=True,widget=forms.TextInput(attrs={'placeholder': 'Min'}))
	carbohydrates_max= forms.IntegerField(label="carbohydrates_max",required=True,widget=forms.TextInput(attrs={'placeholder': 'Max'}))
	protein_min= forms.IntegerField(label="protein_min",required=True,widget=forms.TextInput(attrs={'placeholder': 'Min'}))
	protein_max= forms.IntegerField(label="protein_max",required=True,widget=forms.TextInput(attrs={'placeholder': 'Max'}))


	def __init__(self, *args, **kwargs):
		super(macro_calorie_form, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_show_labels = False 



class contact_form(forms.Form):

	email= forms.CharField(label="Email")
	subject= forms.CharField(label="Subject")
	message= forms.CharField(label="Message")