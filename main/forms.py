# main/forms.py

from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='アップロードしたい画像を選択')
