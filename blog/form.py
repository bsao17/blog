from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.SlugField(required=False)
    date = forms.DateField(widget=forms.DateInput, required=False)
    content = forms.CharField(max_length=255, widget=forms.Textarea)
    published = forms.BooleanField(widget=forms.CheckboxInput())
    image = forms.ImageField(required=False)
