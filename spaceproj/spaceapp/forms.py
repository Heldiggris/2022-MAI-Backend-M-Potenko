from django import forms
from .models import Planet

class PlanetForm(forms.ModelForm):
    class Meta:        
        model = Planet        
        fields = ['name']
    def clean(self):
        data = self.cleaned_data["name"]
        if (len(data) < 3):
            self.add_error('name', 'Слишком короткое название')
            raise ValidationError("Слишком короткое название")
        return data
