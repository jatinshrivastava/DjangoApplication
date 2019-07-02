from django import forms

class uploadFileForm(forms.Form):
	#title = forms.CharField(max_length=50)
	file = forms.FileField()
	shapeType = forms.CharField()
	authorName = forms.CharField()
	fontSize = forms.CharField()
	Left = forms.CharField()
	Top = forms.CharField()
	Height = forms.CharField()
	Width = forms.CharField()