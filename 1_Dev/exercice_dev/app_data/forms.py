from django.forms import ModelForm, Form, CharField
from app_data.models import Annonce


# Creating the form
class Form_Annonce(ModelForm):
    class Meta:
        model = Annonce
        fields = ['departement', 'ville', 'code_ville']


class Form_Add(Form):
    lien = CharField(max_length=1000)
