from django.forms import ModelForm
from django import forms
from .models import *

class CategoryForm(ModelForm):
  class Meta:
    model = Category
    fields = ['title', 'description']
  
  def __init__(self, *args, **kwargs):
    super(CategoryForm, self).__init__(*args, **kwargs)
    self.fields['title'].widget.attrs['class'] = 'form-control'
    self.fields['title'].widget.attrs['v-model'] = 'title'
    self.fields['description'].widget.attrs['class'] = 'form-control'

class BookmarkForm(ModelForm):
  class Meta:
    model = Bookmark
    fields = ['title', 'description', 'url']
  
  def __init__(self, *args, **kwargs):
    super(BookmarkForm, self).__init__(*args, **kwargs)
    self.fields['title'].widget.attrs['class'] = 'form-control'
    self.fields['title'].widget.attrs['v-model'] = 'title'
    self.fields['url'].widget.attrs['class'] = 'form-control'
    self.fields['url'].widget.attrs['v-model'] = 'url'
    self.fields['description'].widget.attrs['class'] = 'form-control'