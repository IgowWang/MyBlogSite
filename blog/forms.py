from django.forms import ModelForm,forms
from .models import Articles
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import  Layout,Div,Field,Submit


class CreateArticleForm(ModelForm):

    class Meta:
        model = Articles
        fields = ['title','content','class_name','tags']

    def __init__(self,*args,**kwargs):
        super(CreateArticleForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method='POST'
        self.helper.form_action='/blog/'
        self.helper.layout=Layout(
            Div(
                Div(
                    Field('title',css_class="form-control", id="title"),
                    Field('content',style="width:1000px;height:1000px;",css_class="ckeditor"),
                    Field('class_name'),
                    Field('tags'),
                    Submit('submit', '提交', css_class='btn btn-default btn-block'),

                    css_class="col-md-8"
                ),
                css_class="row"
            )

        )









