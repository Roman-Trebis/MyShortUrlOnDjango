from django import forms
from .models import Link

class CreateLink(forms.ModelForm):
    long_link = forms.CharField(label='Ваша длинная ссылка:',
    widget=forms.TextInput(attrs={'placeholder': 'Введите свою ссылку'}))
    short_link = forms.CharField(label='Готовая ваша сокращенная ссылка:',
    widget=forms.TextInput(attrs={'placeholder': 'Введите любое слово сокращение'}))

    class Meta:
        model = Link
        fields = ['long_link', 'short_link']
