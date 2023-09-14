from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ModelParser
from .serializer import ModelParserSerializer
from .parser import parse_rss_feed
class ModelParserView(APIView):
    def get(self, request):
        articles = ModelParser.objects.all()
        serializer = ModelParserSerializer(articles, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ModelParserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            items = parse_rss_feed(serializer.validated_data['link'])
            for item in items :
                item.save()
            articles = ModelParser.objects.all()
            serializer = ModelParserSerializer(articles, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)