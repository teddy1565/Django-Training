from .models import GameModel
from rest_framework import serializers

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameModel
        fields = ["url","uid"]