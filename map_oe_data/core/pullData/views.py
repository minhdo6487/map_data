from django.conf import settings
import os
import requests
import subprocess

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class MapDataPull(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        patient_id = kwargs.get("patient_id")
        session_id = kwargs.get("session_id")
        module_name = kwargs.get("module_name")
        fullpath = os.path.join(settings.MAP_DATA_URL, str(patient_id), session_id, module_name)
        res = requests.get(fullpath, verify=False)
        return Response(res.json(), status=status.HTTP_200_OK)


class MapProxy(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):
        path = request.data.get("path")
        try:
            subprocess.call(["bash", "{path}".format(path=path), ])
        except Exception as e:
            return Response({"errors": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"done"}, status=status.HTTP_202_ACCEPTED)
