from django import forms
from .models import Product, Category, SkinType


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Populate Category choices
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

        # Populate SkinType choices
        skin_types = SkinType.objects.all()
        friendly_skin_types = [(st.id, st.get_friendly_name())
                               for st in skin_types]
        self.fields['skin_types'].choices = friendly_skin_types

        # both Classes
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-form'
