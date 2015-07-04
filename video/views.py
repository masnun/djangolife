from django.shortcuts import render
from django.http.response import HttpResponse

from .models import Video

# Create your views here.
def home(request):
    last_video = Video.objects.all().order_by("-id")[0]
    return render(request, 'home.html', {'last_video': last_video})
