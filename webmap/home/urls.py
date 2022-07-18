from django.urls import path, include                                                                                                                            
from .views import home_view
#from django.views.generic import TemplateView


urlpatterns = [ 
    # path('', TemplateView.as_view(template_name="home.html")),
    path('', home_view, name='home'),
    ]