from django.forms import ModelForm
from cream.models import Larek,IceCream

class larekForm(ModelForm):
    class Meta:
        model = Larek
        fields = ('larek_name',)

class creamForm(ModelForm):
    class Meta:
        model = IceCream
        fields = ('name','larek')