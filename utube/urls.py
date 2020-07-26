from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', include(("u_tube.urls", "u_tube"), namespace='videos')),
    path('dashboard/',include(("dashboard.urls", "dashboard"), namespace='dashboard')),
    url(r'^logout/$',auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(("accounts.urls","accounts"), namespace="accounts")),
    url(r'^$', login_required(TemplateView.as_view(template_name="u_tube/video_list.html"))),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)




