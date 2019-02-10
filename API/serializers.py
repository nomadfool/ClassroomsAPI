from rest_framework import serializers
from classes.models import Classroom

class classesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'subject',
            'year',
            'teacher',
            ]


class classesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class classesCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'name',
            'subject',
            'year'
        ]