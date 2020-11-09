from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Sup, yo!</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse(f"<h1>Tweet {tweet_id}!</h1>")