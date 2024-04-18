from django import forms
from .models import Products

class PostForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        labels = {
            'title' : '상품명',
            'content' : '상품 설명',
            'price' : '가격',
        }