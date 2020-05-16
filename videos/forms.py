from django import forms


from .models import Video


class UploadVideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['title', 'description',
                  'video', 'tags', 'categories']
        labels = {
            'video': "Select a video",
        }
        help_text = {
            'video': "Max 4 megabytes",
        }
