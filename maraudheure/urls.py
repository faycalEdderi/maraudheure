from django.contrib import admin
from django.urls import path,include
from users import views as users_views
from maraude import views as maraude_views
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.home, name='home'),
    path("deconnexion/", LogoutView.as_view(), name="logout"),
    path('connexion', users_views.connexion, name='connexion'),

    path('maraudes/', include('maraude.maraude_url')),
    path('users/', include('users.user_url')),

    path('maps', include('maps.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)