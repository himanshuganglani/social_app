from django import forms
from models import Post,Comment

class PostForm(forms.ModelForm):
	description = forms.CharField(required=True)
	title = forms.CharField(required=True)
	image = forms.FileField(required=True)

	class Meta:
		model = Post
		exclude = ['thumbnail']
		fields=('title','description','image',)

class CommentForm(forms.ModelForm):
	comment = forms.CharField(required=True)
	class Meta:
		model = Comment	
		fields = ('comment','post','user')


# class CommentForm(forms.Form):
#     comment = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#         help_text='Write here your message!'
#     )
