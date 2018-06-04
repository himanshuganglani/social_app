from django import forms
from models import Post

class PostForm(forms.ModelForm):
	description = forms.TextField(required=True)
	title = forms.CharField(required=True)
	image = forms.FileField(required=True)

    class Meta:
        model = EntryImage
        exclude = ['thumbnail']
        fields='__all__'