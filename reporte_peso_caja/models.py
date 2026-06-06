# models.py

from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal



class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    code = models.CharField(max_length=20, unique=True, null=True, blank=True)


    def __str__(self):
        return self.user.get_full_name()
    





class Report(models.Model):

    SHIFT = [
        ('shift1', 'Turno 1'),
        ('shift2', 'Turno 2'),
        ('shift3', 'Turno 3'),
        ('shift4', 'Turno 4'),
    ]

    STATES = [
        ('operativa', 'Operativa'),
        ('mantenimiento', 'Mantenimiento'),
        ('reparacion', 'Reparación'),
        ('parada', 'Parada'),
    ]
    MACHINE_CHOICES = [
        ('STICKPACK', 'STICKPACK'),
        ('MULTIPACK1', 'MULTIPACK1'),
        ('MULTIPACK2', 'MULTIPACK2'),
        ('MESPACK', 'MESPACK '),
        ('FLEXPACK0', 'FLEXPACK0'),
        ('FLEXPACK1', 'FLEXPACK1'),
        ('FLEXPACK2', 'FLEXPACK2'),
        ('FLEXPACK3', 'FLEXPACK3'),
        ('VOLPACK', 'VOLPACK'),
    ]

    PRESENTATION = [
        ('Cafe oro 15', 'Cafe oro 15'),
        ('Cafe oro 20', 'Cafe oro 20'),
        ('Cafe oro 45', 'Cafe oro 45'),
        ('Cafe oro 50', 'Cafe oro 50'),
    ]

    shift = models.CharField(
        max_length=20,
        choices=SHIFT
    )
    operator_code =models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    
    machine = models.CharField(
        max_length=200,choices=MACHINE_CHOICES,
    )
    presentation = models.CharField(
        max_length=200,choices=PRESENTATION,null=False, blank=False
        )



    state = models.CharField(
        max_length=20,
        choices=STATES
    )
    

    observation = models.TextField(
        blank=True,
        null=True
    )

    

    creation_date = models.DateTimeField(
        auto_now_add=True
    )

    update_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.machine} - {self.shift}"
    
   

from django.utils import timezone

class ReportDetail(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    box = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    STATUS = [
        ('produccion', 'Producción'),
        ('pausa', 'Pausa'),
        ('terminado', 'Terminado'),
    ]

    status = models.CharField(max_length=20, choices=STATUS, default='produccion')

    observation = models.TextField(blank=True, null=True)