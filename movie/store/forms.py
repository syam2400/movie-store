from django import forms
from store.models import Movies
class movieform(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
