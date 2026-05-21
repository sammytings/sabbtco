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