from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = []

urlpatterns += [
    path('super/user/admin/', admin.site.urls),
    path('', include(('apps.main.mainpage.urls'))),
    path('accounts/', include("allauth.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
