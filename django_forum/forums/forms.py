from django import forms
from .models import Category, Forum, Message, Ad

class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Category
        fields = ['name', 'slug']

class ForumForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False)

    class Meta:
        model = Forum
        fields = ['name', 'description', 'image']
        exclude = ['category'] 

class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False)

    class Meta:
        model = Message
        fields = ['content', 'image']

class AdsForm(forms.ModelForm):
    image = forms.ImageField()
    link = forms.URLField()

    class Meta:
        model = Ad
        fields = ['image', 'link']
    