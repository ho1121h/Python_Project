from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

# Create your views here.
class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all() # sql = selete * from content_feed;
        for _ in feed_list:
            print(_)

        return render(request, 'jinstagram/main.html')

