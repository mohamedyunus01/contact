from django.urls import path
from . import views
from contact import views as contact_views



urlpatterns = [
    path('', contact_views.contact_view, name='contact'),
    path('view_details',contact_views.viewDetails),
    
]