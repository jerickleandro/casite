from django.urls import path
from .views import IndexView, TestetView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('teste', TestetView.as_view(), name='teste'),

]