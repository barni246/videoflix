from django.shortcuts import render, get_object_or_404
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'netflix.html', {'videos': videos})

def stream(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'stream.html', {'video': video})



