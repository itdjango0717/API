from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser, JSONParser
from .serializers import UserSer
from django.core.mail import send_mail
from django.conf import settings

class Signup(APIView):
    parser_classes = [MultiPartParser, JSONParser]
    def get(self, request):
        user = User.objects.all()
        ser = UserSer(user, many=True)
        return Response({'data':ser.data})

    def post(self, request):
        ser = UserSer(data=request.data)
        if ser.is_valid():
            user = ser.save()
            send_mail(
                'AVTOELON',
                'AVTOELON. Bizning brendimizdan foydalanayotganingizdan mamnunmiz. Bizga bergan ishonchingiz uchun tashakkur',
                settings.EMAIL_HOST_USER,
                [user.email]
            )
            return Response(ser.data)
        return Response(ser.errors)

