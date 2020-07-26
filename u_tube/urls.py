from django.urls import path
from u_tube.views import Index, VideoDetail
from django.conf.urls import url

urlpatterns = [
    path('', Index.as_view(), name='list'),
    path('<int:video_id>/', VideoDetail.as_view(), name='detail'),
]




