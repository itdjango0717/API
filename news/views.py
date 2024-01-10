from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser

from .models import Mashina
from .serializers import CarSerializer


class CarApiList(APIView):
    parser_classes = [MultiPartParser]

    def get(self, request):
        t = Mashina.objects.all()
        dict_data = CarSerializer(t, many=True)

        return Response(dict_data.data)

    def post(self, request):
        print(request.data)

        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            m = serializer.save()
            return Response(m.data)
        return Response(serializer.errors)

