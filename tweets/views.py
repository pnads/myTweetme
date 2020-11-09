from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Sup, yo!</h1>")
    return render(request, 'pages/home.html', context={}, status=200)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by Javascript/Swift/Java/iOS/Android
    return JSON data
    """
    data = {
        "id": tweet_id,
    }

    status = 200

    try:
        obj = Tweet.objects.get(id = tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404

    return JsonResponse(data, status=status) #json.dumps content_type='applicationJSON'