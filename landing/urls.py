from django.urls import path
from .views import  Drel1, Dtrel1, Drel2, Dfem1

urlpatterns = [
    path('d-rel-1/', Drel1.as_view(), name='drel1'),
    path('dt-rel-1/', Dtrel1.as_view(), name='dtrel1'), 
    path('d-rel-2/', Drel2.as_view(), name='drel2'),
    path('d-fem-1/', Dfem1.as_view(), name='dfem1'),
    path('d-fem-2/', Dfem1.as_view(), name='dfem2'),
    path('d-fem-3/', Dfem1.as_view(), name='dfem3'),
]