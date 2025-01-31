from django import forms
from lms_app.models import author

class AuthorForm(forms.ModelForm):
    class Meta:
        model=author
        fields='__all__'