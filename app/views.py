from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title": "JDEVS.MX"
    }
    return render(request, "app/index.html", context)


def solutions_view(request):
    context = {}
    return render(request, "app/solutions.html", context)


def signup_view(request):
    context = {}
    return render(request, "app/signup.html", context)
