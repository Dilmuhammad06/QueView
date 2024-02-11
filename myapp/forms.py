from django import forms
from.models import Video

class VideoForms(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name','description','thumbnail','video','slug']