from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

# Non-translated URLs
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

# Translated URLs
urlpatterns += i18n_patterns(
    path('', include('app.urls')),
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)