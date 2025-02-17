from django import forms
from lms_app.models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'