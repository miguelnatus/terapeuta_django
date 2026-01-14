from django.urls import path
from .views import HomeView, HomeView2

urlpatterns = [
    path('d-rel-1/', HomeView.as_view(), name='home'),
    path('dt-rel-1/', HomeView2.as_view(), name='home2'),
]