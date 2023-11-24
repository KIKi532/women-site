from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.utils.text import slugify



class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категорія не вибрана", label="Категорії")


    class Meta:
        model = Women
        fields = ['title', 'content', 'photo', 'is_published', 'cat', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 50:
                raise ValidationError("Довжина більше 50 символів")

            return title


