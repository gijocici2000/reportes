from django.urls import path
from . import views

urlpatterns = [
    # =========================
    # BASE
    # =========================
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # =========================
    # AUTH
    # =========================
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('no-autorizado/', views.not_authorized, name='no_autorizado'),

    # =========================
    # REPORTS
    # =========================
    path('report/create/', views.create_report, name='create_report'),
    path('report/<int:report_id>/', views.read_report, name='read_report'),
    path('report/<int:report_id>/update/', views.update_report, name='update_report'),
    path('report/<int:report_id>/delete/', views.delete_report, name='delete_report'),

    # =========================
    # REPORT DETAILS
    # =========================
    path(
        'report/<int:report_id>/detail/create/',
        views.create_report_detail,
        name='create_report_detail'
    ),

    path(
        'report/<int:report_id>/detail/<int:detail_id>/',
        views.read_report_detail,
        name='read_report_detail'
    ),

    path(
        'report/<int:report_id>/detail/<int:detail_id>/update/',
        views.update_report_detail,
        name='update_report_detail'
    ),

    path(
        'report/<int:report_id>/detail/<int:detail_id>/delete/',
        views.delete_report_detail,
        name='delete_report_detail'
    ),
]