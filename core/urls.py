
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.views.static import serve # esto porque no hay build
from django.conf.urls.static import static
from django.conf import settings
import os


urlpatterns = [
    path('favicon.ico', serve, {'path': 'favicon.ico', 'document_root': os.path.join(settings.BASE_DIR, 'public')}),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('apps.user.urls')),
    
    path('api/pc_isla/', include("apps.pc_isla.urls")),
    path('api/buscador/', include("apps.buscador.urls")),
    path('api/informes/', include("apps.informes.urls")),
    path('api/base/', include("apps.base.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]