from rest_framework import serializers
from .models import FilePathModel

class FilePathSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FilePathModel
        fields = ["url","path"]