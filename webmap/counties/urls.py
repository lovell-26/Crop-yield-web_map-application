from django.urls import path                                                                                                                         
from .views import start_view, graphs_view

urlpatterns = [
    path('', start_view, name='start'),
    path('<county>/<crop>/<field>/', graphs_view, name='graphs')]
    