from rest_framework import serializers
from .models import Planet, Category, Atmosphere
from rest_framework.renderers import JSONRenderer

class AtmosphereSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atmosphere
        fields = ["id", "h2", "he", "h2O", "co2", "n", "o2", "ar", "other"]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"] 


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    # category = serializers.CharField(source='category.name', allow_null=True)
    category = CategorySerializer()
    atmosphere = AtmosphereSerializer()
    class Meta:
        model = Planet
        fields = ["id", "name", "orbit", "category", "atmosphere"] 

