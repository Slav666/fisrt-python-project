from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, request
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat",
    "february": "Walk at least 20 minutes every day",
    "march": "Learn Django at least 20 minutes every day",
    "april": "Learn React at leat 1 hour every day",
    "may": "Mountain climbing",
    "june": "Start to save some money",
    "july": "Do some body exercises",
    "august": "Buy a new car",
    "september": "Start to drink more water",
    "october": "Tidy up my back garden",
    "november": "Start to build a deck",
    "december": None
}


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month_name": month})
    except:
        raise Http404()
