from django.urls import path                                                                                                                         
from .views import crops_view

urlpatterns = [
    path('<crop>/<field>/<int:year>', crops_view, name='crop'),
]