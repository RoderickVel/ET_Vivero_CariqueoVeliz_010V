from rest_framework import serializers
from HildaApp.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=['rut','nombre','direccion','telefono', 'edad']