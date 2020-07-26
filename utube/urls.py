from django.contrib import admin
from django.urls import path, include
from u_tube.views import Index, VideoDetail
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', Index.as_view(), name='list'),
    path('admin/', admin.site.urls),
    path('videos/', include(("u_tube.urls", "u_tube"), namespace='videos')),
    path('dashboard/',include(("dashboard.urls", "dashboard"), namespace='dashboard')),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)




