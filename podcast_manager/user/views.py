from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class RegisterUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@csrf_exempt
@api_view(['GET'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return JsonResponse({'error': 'Please provide username and password'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'success': 'User logged in successfully'}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


