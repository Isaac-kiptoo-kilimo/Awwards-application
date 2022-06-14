from django import forms
from .models import *
from django.forms import ModelForm




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email','fullname','proc_img','bio','contacts']

# class RateForm(forms.ModelForm):
#     class Meta:
#         model = Rate
#         fields = ['design', 'usability', 'content','creativity']


class RateForm(forms.Form):

    rating = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    )
    design = forms.ChoiceField(choices=rating)
    usability =forms.ChoiceField(choices=rating)
    content = forms.ChoiceField(choices=rating)
    creativity =forms.ChoiceField(choices=rating)

    class Meta:
        model = Rate
        fields = ['design', 'usability', 'content','creativity']
   