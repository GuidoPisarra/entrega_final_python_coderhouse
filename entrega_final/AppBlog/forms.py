from django import forms


class New_post(forms.Form):
    title = forms.CharField(max_length=30)
    sub_title = forms.CharField(max_length=30)
    content = forms.CharField(max_length=1500, widget=forms.Textarea)
    imagen = forms.ImageField(required=False)


class Form_search_post(forms.Form):
    search_post = forms.CharField(max_length=100)
