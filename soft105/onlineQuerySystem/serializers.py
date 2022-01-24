from rest_framework import serializers
from .models import Users,Question

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ["url","account","password"]

class QuestioinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["url","account","inputText"]