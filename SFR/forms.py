from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    is_series = forms.BooleanField(label='Search for series', required=False)
