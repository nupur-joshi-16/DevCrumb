from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")


# Dynamic URL

monthly_challenges = {
    "january": "Challenge for January: Read a new book.",
    "february": "Challenge for February: Exercise for 30 minutes daily.",
    "march": "Challenge for March: Learn a new skill.",
    "april": "Challenge for April: Practice meditation.",
    "may": "Challenge for May: Drink more water daily.",
    "june": "Challenge for June: Reduce screen time.",
    "july": "Challenge for July: Wake up early.",
    "august": "Challenge for August: Maintain a gratitude journal.",
    "september": "Challenge for September: Improve coding skills.",
    "october": "Challenge for October: Try a new hobby.",
    "november": "Challenge for November: Eat healthy meals.",
    "december": "Challenge for December: Reflect on the year's progress."
}


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not found!")
    
# def monthly_challenge(request, month):
#     challenge_text = None
#     if month == 'january':
#         challenge_text = "Eat no meat for the entire month!"
#     elif month == 'february':
#         challenge_text = "Walk for at least 20 minutes every day!"
#     else:
#         return HttpResponseNotFound("This month is not supported!")
#     return HttpResponse(challenge_text)