from django import views
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from main import views

from main.views import IndexPageView, ChangeLanguageView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),
    
    path('lab1/',views.lab1, name='lab1'),
    path('lprofile/',views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
