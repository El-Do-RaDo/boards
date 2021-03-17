from django import forms
from boards.models import Topic
from boards.models import Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'placeholder': 'Add your message here.'}
        ), max_length=4000)

    class Meta:
        model = Topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message',]