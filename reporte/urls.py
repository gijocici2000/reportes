from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Tus apps
    path('', include('reporte_peso_caja.urls')),

    

    # Recuperación de contraseña
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registro_usuario/password_reset.html'
        ),
        name='password_reset'
    ),

    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registro_usuario/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registro_usuario/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registro_usuario/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]


