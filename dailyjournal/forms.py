from django import forms
from django.forms import DateInput
from .models import JournalLog
from cloudinary.forms import CloudinaryFileField

"""
Form for creating and updating a journal. 
The user can specify the date when the journal was created, and add content to 
their journal. 
"""

RATING_OPTIONS = (
    ('Amazing', 'Amazing'),
    ('Good', 'Good'),
    ('Okay', 'Okay'),
    ('Bad', 'Bad'),
    ('Awful', 'Awful'),

)


class JournalForm(forms.ModelForm):

    rating = forms.CharField(
        max_length=20,
        widget=forms.Select(attrs={'id': 'id_rating'}, choices=RATING_OPTIONS),
        initial='Okay',
    )

    image = CloudinaryFileField(required=False, 
    widget=forms.ClearableFileInput(attrs={'id': 'id_image'})
    )

    class Meta:
        model = JournalLog
        fields = ['created_on', 'content', 'rating', 'image']
        ordering = ['-created_on']
        widgets = {
            'created_on': DateInput(attrs={'type': 'date'}),
            'content': forms.Textarea(attrs={
                'placeholder': "What's on your mind today?",
                'class': 'form-control textarea-form-content',
                'id': 'id_content'
            }),
            'rating': forms.Select(choices=RATING_OPTIONS),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }
