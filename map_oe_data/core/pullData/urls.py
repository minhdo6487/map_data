from django.urls import path

from .views import MapDataPull, MapProxy


urlpatterns = [
    path("data-pull/<int:patient_id>/<str:session_id>/<str:module_name>", MapDataPull.as_view()),
    path("map-proxy/", MapProxy.as_view())
]
