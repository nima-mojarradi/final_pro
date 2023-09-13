from rest_framework import serializers
from .models import ModelParser

class ModelParserSerializer(serializers.ModelSerializer):
    description = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    class Meta:
        model = ModelParser
        fields = ('link','description','title')