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
