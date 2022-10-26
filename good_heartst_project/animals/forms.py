from dataclasses import field
from django import forms
from .models import Category, MainAnimals


class PostForm(forms.ModelForm):
    class Meta:
        model = MainAnimals
        fields = ['title', 'contents', 'potho', 'category']
