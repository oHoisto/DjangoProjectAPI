from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Заголовок",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "id": "title",
        })
    )

    content = forms.CharField(
        label="Содержание",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "id": "content",
            "rows": 6,
        })
    )

    author = forms.CharField(
        max_length=100,
        label="Автор",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "id": "author",
        })
    )