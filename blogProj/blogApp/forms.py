from django import forms


class BlogForm(forms.Form):
    user_id = forms.IntegerField(required=False, label='id')
    author = forms.CharField(required=False, label='автор')
    title = forms.CharField(required=False, label='название')
    text = forms.SlugField()
    count = forms.IntegerField()
