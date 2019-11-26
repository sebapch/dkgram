#POST FORMS

#DJANGO
from django import forms

#MODELS
from posts.models import Post 

class PostForm(forms.ModelForm):
	#POST MODEL FORM

	class Meta:
		#FORM SETTINGS

		model = Post
		fields = ('user', 'profile', 'title', 'photo')