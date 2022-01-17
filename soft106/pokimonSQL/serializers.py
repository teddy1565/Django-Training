from .models import Pokemon
from rest_framework import serializers

class HomePageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["url"]

class addPokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["url","uid","name","position","pokemonType"]