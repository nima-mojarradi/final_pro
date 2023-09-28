from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Like, ModelParser

class LikedPosts(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user)
        liked_post = Like.objects.filter(user=user)
        if liked_post:
            podcast_ids = [like.podcast.id for like in liked_post]
            podcasts = ModelParser.objects.filter(id__in=podcast_ids)
            return Response(podcasts)
        else:
            return Response([])



