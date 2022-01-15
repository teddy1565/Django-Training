from .models import GameModel,GameContentModel
from rest_framework import serializers

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameModel
        fields = ["url","uid"]

class GameContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameContentModel
        fields = ["url"]