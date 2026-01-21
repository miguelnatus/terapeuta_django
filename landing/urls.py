from django.urls import path
from .views import  Drel1, Dtrel1

urlpatterns = [
    path('d-rel-1/', Drel1.as_view(), name='drel1'),
    path('dt-rel-1/', Dtrel1.as_view(), name='dtrel1'), 
]