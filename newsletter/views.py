from django.shortcuts import render

# Create your views here.
def home(request):
    title = "My Django site"
    context = {

    }
    return render(request, "home.html", context)
