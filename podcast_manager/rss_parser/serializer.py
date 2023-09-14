from rest_framework import serializers
from .models import ModelParser

class ModelParserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelParser
        fields = ('link','description','title')
        extra_kwargs = {
            'description':{'read_only':True},
            'title':{'read_only':True}
        }