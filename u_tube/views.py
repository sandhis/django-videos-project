from django.shortcuts import render
from django.views import generic
from u_tube.models import Video
# Create your views here.

class Index(generic.ListView):
    template_name = 'templates/u_tube/video_list.html'
    model = Video
    context_object_name = 'videos'
    ##queryset = Video.objects.filter(title__contains = 'sample')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["video_active"] ="active"
        return context


class VideoDetail(generic.DetailView):
    template_name = 'u_tube/video_detail.html'
    model = Video
    pk_url_kwarg = 'video_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["video_active"] ="active"
        return context
