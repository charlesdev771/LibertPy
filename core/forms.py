from django import Forms 

from .models import Coments

class ComentForm(form.ModelForm):
    class Meta:
        model = Coments
        fields = ['name', 'comment']