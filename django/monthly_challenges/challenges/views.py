from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import HttpResponse,render
from django.urls import reverse

# Create your views here.
monthly_challenge_text = {
    "january":"This is January challenge",
    "february":"This is Feb challenge",
    "march": "This is march challenge"
}
def index(request):
    month_keys = monthly_challenge_text.keys();
    month_string="";
    for month in month_keys:
        month_name = month.capitalize();
        month_url = reverse("month_challenge", args=[month]);
        month_string+= f"<li><a href=\"{month_url}\">{month_name}</a></li>"
    return HttpResponse(month_string)

def monthly_challenges(request, month):
    challenge_text=None;
    try:
        challenge_text=monthly_challenge_text[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month not supported")
