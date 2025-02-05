from django import forms
from django.core.exceptions import ValidationError

from .models import Brand, Category, Product, ProductImage


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ()


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        exclude = ()


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('pub_date',)


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']

    def clean(self):
        cleaned_data = super().clean()
        product = self.instance.product

        if product and product.images.count() == 0:
            raise ValidationError(
                'Минимальное количество фотографий для товара - 1.'
            )

        elif product and product.images.count() >= 5:
            raise ValidationError(
                'Максимальное количество фотографий для товара - 5.'
            )

        return cleaned_data

ProductImageFormSet = forms.inlineformset_factory(
    Product, ProductImage, form=ProductImageForm, extra=5, max_num=5
)
