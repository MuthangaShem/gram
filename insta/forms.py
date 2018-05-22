from django import forms
from .models import Profile, Image, Comment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageUpload(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['post_date', 'image_owner']

class profileEdit(forms.Form):
    name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    website = forms.URLField(initial='http://')
    Bio = forms.Textarea()
    Email = forms.EmailField()
    phone_number = forms.CharField(max_length=12)
    Gender = forms.CharField(max_length=6)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)
        widgets = {
            'comment_content': forms.TextInput(attrs={
                'class': u'comments-input form-control', 'placeholder': u'Insert Comment'})
        } 