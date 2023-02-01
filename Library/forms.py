from Library.models  import Books
from django import forms

class BookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = '__all__'
        
       