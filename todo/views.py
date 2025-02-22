from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    context = {
        "title": "To Do",
    }
    return render(request, "cards/to_do_card.html" , context)
def hero(request):
    context = {
        "title": "To Do",
    }
    return render(request, "heroes/hero.html")

def main(request):
    context = {
        "title": "To Do",
    }
    return render(request, "main.html")