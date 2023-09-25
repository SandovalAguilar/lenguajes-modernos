from django.urls import path
from principal_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path('list', views.VendedorList.as_view(),
         name='vendedor_list'),
    path('view/<int:pk>', views.VendedorView.as_view(),
         name='vendedor_list'),
    path('new', views.VendedorCreate.as_view(),
         name='vendedor_create'),
    path('view/<int:pk>', views.VendedorView.as_view(),
         name='vendedor_view'),
    path('edit/<int:pk>', views.VendedorUpdate.as_view(),
         name='vendedor_update'),
    path('delete/<int:pk>', views.VendedorDelete.as_view(),
         name='vendedor_delete'),
    path('inmueble/list', views.InmuebleList.as_view(),
         name='inmueble_list'),
    path('inmueble/view/<int:pk>', views.InmuebleView.as_view(),
         name='inmueble_list'),
    path('inmueble/new', views.InmuebleCreate.as_view(),
         name='inmueble_create'),
    path('inmueble/edit/<int:pk>', views.InmuebleUpdate.as_view(),
         name='inmueble_update'),
    path('inmueble/delete/<int:pk>',
         views.InmuebleDelete.as_view(), name='inmueble_delete'),
]
