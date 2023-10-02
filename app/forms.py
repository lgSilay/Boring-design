from django import forms

from app.models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
