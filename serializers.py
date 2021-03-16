from rest_framework import serializers
from app.models import Peri

class BasicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Peri
        fields=['id','radius']