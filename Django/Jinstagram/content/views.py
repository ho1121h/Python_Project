from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

# Create your views here.
class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # sql = selete * from content_feed; / 역순정렬

  
        return render(request, 'jinstagram/main.html', context=dict(feeds=feed_list))

