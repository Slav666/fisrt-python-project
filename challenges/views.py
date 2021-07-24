from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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
    "december": "Paint a whole house"
}


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
        response_data = f"<h1>{challenge_text}<h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported")
