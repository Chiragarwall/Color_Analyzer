# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import color_analyzer

urlpatterns = [
    path('', color_analyzer, name='color_analyzer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
