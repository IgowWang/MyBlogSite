from django.shortcuts import render
from .forms import SignUpForm
import django
# Create your views here.
def home(request):
    title = "Welcome"
    if request.user.is_authenticated():
        title = "My Title %s" %(request.user)
    #add a form
    form = SignUpForm(request.POST or None)
    context = {
        "template_title" : title,
        "form":form

    }

    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.full_name :
            instance.full_name ="wang"

        instance.save()
        context = {
                "template_title":"Thank you"
                }
    return render(request,"base1.html",context)
