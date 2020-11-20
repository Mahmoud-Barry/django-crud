from django import forms

class UserRegister(forms.Form):
    libelle = forms.CharField(required= True,
        widget=forms.TextInput(
            attrs={'class': "form-control" 
            }
        ))
    pu = forms.CharField(required= True,
        widget=forms.TextInput(
            attrs={'class':"form-control"}
        ))
    qte = forms.CharField(required= True,
        widget=forms.TextInput(
            attrs={'class': "form-control"}
        ))
    seuil = forms.CharField(required= True,
        widget=forms.TextInput(
            attrs={'class': "form-control"}
        ))
