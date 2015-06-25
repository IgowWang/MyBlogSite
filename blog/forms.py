from django.forms import ModelForm
from .models import Articles

class CreateArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','content','class_name','tags']



