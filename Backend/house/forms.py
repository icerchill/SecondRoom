from django import forms
from .models import Room, Room_img

class RoomForm(forms.ModelForm):
    zipcode = forms.CharField(max_length=10, label="zipcode")
    price = forms.IntegerField()
    landmark = forms.CharField(max_length=250)
    long_term_lease = forms.BooleanField
    start_date = forms.DateField(input_formats=['%m/%d/%Y'])
    description = forms.CharField(max_length=1000)
    class Meta:
        model = Room
        fields = (
            'zipcode',
            'price',
            'landmark',
            'long_term_lease',
            'start_date',
            'description',
        )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label="Image")
    class Meta:
        model = Room_img
        fields = (
            'image',
        )