from django import forms

from app.models import Commentary


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea)

    class Meta:
        model = Commentary
        fields = ("content",)
