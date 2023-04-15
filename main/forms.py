from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Para,Teacher
from dal import autocomplete

class ParaForm(forms.ModelForm):
    date = forms.IntegerField(required=True)
    period = forms.IntegerField(required=True)
    nameC = forms.CharField(max_length=500, required=True)
    categ = forms.CharField(max_length=100, required=True)
    nameT = forms.CharField(max_length=50,required=True)
    place = forms.CharField(max_length=500,required=True)
    
    class Meta:
        model = Para
        fields = ['date', 'period', 'nameC', 'categ', 'nameT', 'place']
        
class TeacherForm(forms.ModelForm):
    nameT = forms.CharField(max_length=50,required=True)

    class Meta:
        model = Teacher
        fields = ['nameT']


class ReqForm(forms.ModelForm):
    ID = forms.ModelChoiceField(required=True, queryset=Teacher.objects.all(), widget=autocomplete.ModelSelect2(url='autocomplete'))
    nedelya = forms.IntegerField(required=True, min_value=1, max_value=16)
    class Meta:
        model = Teacher
        fields = ['ID']
        widgets = {
            'ID': autocomplete.ModelSelect2(url='autocomplete')
        }