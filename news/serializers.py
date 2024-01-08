from rest_framework import serializers

from .models import Mashina


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mashina
        fields = ['id', 'rusumi', 'Yoqilgi', 'Narxi', 'Turi', 'Yana', 'rasm', 'Rang', 'Peredacha', 'Obyom']
        read_only_fields = ['id', 'Narxi']

    # def create(self, validated_data):
    #     print(validated_data)
    #
    #     rusumi = validated_data.get('rusumi', None)
    #     narxi = validated_data.get('narxi', None)
    #     m = Mashina.objects.create(
    #         rusumi=rusumi,
    #         narxi=narxi,
    #     )
    #     return m

    def update(self, instance, validated_data):
        print(instance)
        instance.rusumi = validated_data.get('rusumi', instance.rusumi)
        instance.narxi = validated_data.get('narxi', instance.narxi)
        instance.save()
        return instance
