from django.urls import path

from .views import MapDataPull, MapProxy


urlpatterns = [
    path("edb/<int:patient_id>/<str:session_id>/<str:module_name>", MapDataPull.as_view()),
    path("edb/map-proxy/", MapProxy.as_view())
]
