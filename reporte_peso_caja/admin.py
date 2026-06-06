from django.contrib import admin
from .models import Employee, Role, Report, ReportDetail
# Register your models here.

admin.site.site_header = "Admin Panel - Reporte Peso Caja"
admin.site.site_title = "Reporte Peso Caja Admin"
admin.site.index_title = "Bienvenido al Panel de Administración de Reporte Peso Caja"
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Report)
admin.site.register(ReportDetail)
