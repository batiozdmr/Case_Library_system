from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'image',
            'publication_date'
        ]

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for arr in self.fields:
            if arr == "publication_date":
                self.fields[arr].widget.attrs = {'class': 'form-control ', 'autocomplete': 'off',
                                                 'placeholder': 'gg.aa.yyyy', 'data-date-format': 'dd.mm.yyyy', }
            else:
                self.fields[arr].widget.attrs = {'class': 'form-control'}
