from django.contrib import admin
from .forms import SignUpForm
# Register your models here.
from .models import SignUp
class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__","timestamp","updated"]
    form = SignUpForm
admin.site.register(SignUp,SignUpAdmin)
