from django import forms

from petstagram.common.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', ]

        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...',
                }
            ),
        }


class SearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by pet name...',
            }
        )
    )