from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from .forms import CustomUserCreationForm, ReportForm, ReportDetailForm
from .models import Report, ReportDetail

# =========================
# DASHBOARD
# =========================
@login_required
def index(request):

    return render(
        request,
        'index.html'
    )

# =========================
# REGISTRO
# =========================
@login_required
def register_view(request):

    if request.method == 'POST':

        form = CustomUserCreationForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Usuario registrado correctamente.'
            )

            return redirect('login')

    else:

        form = CustomUserCreationForm()

    return render(
        request,
        'registro_usuario/register.html',
        {
            'form': form
        }
    )


# =========================
# LOGIN
# =========================
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "registro_usuario/login.html", {"form_errors": True})

    return render(request, "registro_usuario/login.html")


# =========================
# LOGOUT
# =========================

@login_required
def logout_view(request):

    logout(request)

    return redirect('login')


# =========================
# NO AUTORIZADO
# =========================
def not_authorized(request):

    return render(
        request,
        'registro_usuario/not_authorized.html',
        {
            'message':
                'No tienes permitido el acceso.'
        }
    )





@login_required
def dashboard(request):

    reports = Report.objects.all()

    return render(request, 'dashboard.html', {
        'reports': reports
    })


# =========================
# CREATE REPORT
# =========================

@login_required
def create_report(request):

    shift = request.GET.get('shift', 'shift1')

    if request.method == 'POST':

        form = ReportForm(request.POST)

        if form.is_valid():
            report = form.save()
            return redirect('create_report_detail', report_id=report.id)

    else:

        form = ReportForm(initial={
            'shift': shift
        })

    return render(request, 'box_report/create_report.html', {
        'form': form
    })


@login_required
def read_report(request, report_id):

    report = Report.objects.get(id=report_id)

    return render(
        request,
        'read_report.html',
        {
            'report': report
        }
    )
@login_required
def update_report(request, report_id):
    report = Report.objects.get(id=report_id)

    if request.method == 'POST':

        form = ReportForm(
            request.POST,
            instance=report
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Reporte actualizado correctamente.'
            )

            return redirect('dashboard')

    else:

        form = ReportForm(instance=report)

    return render(
        request,
        'box_register/update_report.html',
        {
            'form': form,
            'report': report
        }
    )


@login_required
def delete_report(request, report_id):

    report = Report.objects.get(id=report_id)

    if request.method == 'POST':

        report.delete()

        messages.success(
            request,
            'Reporte eliminado correctamente.'
        )

        return redirect('dashboard')

    return render(
        request,
        'box_register/delete_report.html',
        {
            'report': report
        }
    )



from django.db.models import Sum

@login_required
def create_report_detail(request, report_id):

    report = get_object_or_404(Report, id=report_id)

    form = ReportDetailForm()  # ✔ siempre existe

    if request.method == 'POST':

        form = ReportDetailForm(request.POST)

        if form.is_valid():

            detail = form.save(commit=False)

            detail.report = report
            detail.registered_by = request.user
            detail.start_time = timezone.now()

            detail.save()

            return redirect('create_report_detail', report_id=report.pk)

    # 🔥 HISTORIAL
    details = ReportDetail.objects.filter(report=report).order_by('-id')

    # 🔥 DASHBOARD PRO (CORREGIDO)
    total_boxes = details.count()

    total_weight = details.aggregate(
        total=Sum('weight')
    )['total'] or 0

    return render(request, 'box_report_detail/create_report_detail.html', {
        'report': report,
        'form': form,
        'details': details,
        'total_boxes': total_boxes,
        'total_weight': total_weight,
    })
@login_required
def read_report_detail(request, report_id, detail_id):

    detail = ReportDetail.objects.get(id=detail_id, report_id=report_id)

    return render(
        request,
        'read_report_detail.html',
        {
            'detail': detail
        }
    )
@login_required
def update_report_detail(request, report_id, detail_id):

    detail = ReportDetail.objects.get(id=detail_id, report_id=report_id)

    if request.method == 'POST':

        form = ReportDetailForm(
            request.POST,
            instance=detail
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Detalle de reporte actualizado correctamente.'
            )

            return redirect('read_report', report_id=report_id)

    else:

        form = ReportDetailForm(instance=detail)

    return render(
        request,
        'update_report_detail.html',
        {
            'form': form,
            'detail': detail
        }
    )
@login_required
def delete_report_detail(request, report_id, detail_id):

    detail = ReportDetail.objects.get(id=detail_id, report_id=report_id)

    if request.method == 'POST':

        detail.delete()

        messages.success(
            request,
            'Detalle de reporte eliminado correctamente.'
        )

        return redirect('read_report', report_id=report_id)

    return render(
        request,
        'delete_report_detail.html',
        {
            'detail': detail
        }
    )
