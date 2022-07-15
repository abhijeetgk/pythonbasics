from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import HttpResponse,render

# Create your views here.
monthly_challenge_text = {
    "january":"This is January challenge",
    "february":"This is Feb challenge",
    "march": "This is march challenge"
}

def monthly_challenges(request, month):
    challenge_text=None;
    try:
        challenge_text=monthly_challenge_text[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month not supported")
