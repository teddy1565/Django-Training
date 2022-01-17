from rest_framework import serializers
from .models import PWD

class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PWD
        fields = ["url","password"]