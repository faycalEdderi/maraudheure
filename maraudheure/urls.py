from django.contrib import admin
from django.urls import path,include
from users import views as users_views
from maraudheure import views
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
    path("reset_password", PasswordResetView.as_view(), name='reset_password'),
    path("reset_password/done", PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('select/type/account', views.account_type, name='account_type'),
    path('contact', views.contact, name='contact'),

    path('maraudes/', include('maraude.maraude_url')),
    path('users/', include('users.user_url')),

    path('maps', include('maps.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)