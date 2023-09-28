from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import LikedPodcastsSerializer
from .models import Like, ModelParser

class LikedPodcasts(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        liked_podcasts = Like.objects.filter(user=user)
        serializer = LikedPodcastsSerializer(liked_podcasts, many=True)
        return Response(serializer.data)


