from rest_framework import serializers

from .models import Mashina, Rusumi, Rang, Rasm, Yoqilgi, Peredacha, Obyom, Kuzov, Narxi, Turi, Yana


class GetRusumi(serializers.ModelSerializer):
    class Meta:
        model = Rusumi
        fields = ['marka']


class GetYana(serializers.ModelSerializer):
    class Meta:
        model = Yana
        fields = ['content']


class GetRang(serializers.ModelSerializer):
    class Meta:
        model = Rang
        fields = ['name']


class GetRasm(serializers.ModelSerializer):
    class Meta:
        model = Rasm
        fields = ['rasm']


class GetYoqilgi(serializers.ModelSerializer):
    class Meta:
        model = Yoqilgi
        fields = ['name']


class GetPeredacha(serializers.ModelSerializer):
    class Meta:
        model = Peredacha
        fields = ['peredacha']


class GetObyom(serializers.ModelSerializer):
    class Meta:
        model = Obyom
        fields = ['obyom']


class GetKuzov(serializers.ModelSerializer):
    class Meta:
        model = Kuzov
        fields = ['turi']


class GetNarxi(serializers.ModelSerializer):
    class Meta:
        model = Narxi
        fields = ['narxi']


class GetTuri(serializers.ModelSerializer):
    class Meta:
        model = Turi
        fields = ['name']


class CarSerializer(serializers.ModelSerializer):
    rusumi = GetRusumi()
    Yoqilgi = GetYoqilgi()
    Narxi = GetNarxi()
    Turi = GetTuri()
    Yana = GetYana()
    rasm = GetRasm()
    Peredacha = GetPeredacha()
    Obyom = GetObyom()

    class Meta:
        model = Mashina
        fields = ['id', 'rusumi', 'Yoqilgi', 'Narxi', 'Turi', 'Yana', 'rasm', 'Rang', 'Peredacha', 'Obyom']

