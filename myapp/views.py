from django.shortcuts import render,get_object_or_404,redirect
from .models import Video
from .forms import VideoForms

def index(request):
    video = Video.objects.all()
    data = {
        'videos':video
    }
    return render(request,'index.html',context=data)


def video_view(request, video_slug):
    video = get_object_or_404(Video, slug=video_slug)
    data = {'video': video}
    return render(request, 'video_view.html', context=data)


def posting(request):
    if request.method == 'POST':
        form = VideoForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = VideoForms()

    return render(request,'posting.html',{'form':form})