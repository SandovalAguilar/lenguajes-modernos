from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from datetime import datetime
import re

from principal_app.models import Vendedor
from principal_app.models import Inmueble

from datetime import datetime


def home(request):
    return HttpResponse("Hello, Django!")


def date_view(request, name):
    return render(
        request,
        'principal_app/date_view.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


class VendedorList(ListView):
    model = Vendedor


class VendedorView(DetailView):
    model = Vendedor


class VendedorCreate(CreateView):
    model = Vendedor
    fields = ['id_vendedor', 'nombre']
    success_url = reverse_lazy('vendedor_list')


class VendedorUpdate(UpdateView):
    model = Vendedor
    fields = ['id_vendedor', 'nombre']
    success_url = reverse_lazy('vendedor_list')


class VendedorDelete(DeleteView):
    model = Vendedor
    success_url = reverse_lazy('vendedor_list')


class InmuebleList(ListView):
    model = Inmueble


class InmuebleView(DetailView):
    model = Inmueble


class InmuebleCreate(CreateView):
    model = Inmueble
    fields = ['id_inmueble', 'id_tipo',
              'id_operacion', 'id_provincia', 'superficie',
              'precio_venta'
              ]
    readonly_fields = ['fecha_alta']
    success_url = reverse_lazy('inmueble_list')


class InmuebleUpdate(UpdateView):
    model = Inmueble
    fields = ['id_inmueble', 'id_tipo',
              'id_operacion', 'id_provincia', 'superficie',
              'precio_venta', 'fecha_venta', 'id_vendedor'
              ]
    readonly_fields = ['fecha_alta']
    success_url = reverse_lazy('inmueble_list')


class InmuebleDelete(DeleteView):
    model = Inmueble
    success_url = reverse_lazy('inmueble_list')
