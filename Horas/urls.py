from django.urls import path
from .views import HorasListView

app_name="Horas"

urlpatterns = [
    #vistas de horas
    path('', HorasListView.as_view(), name="home")
]