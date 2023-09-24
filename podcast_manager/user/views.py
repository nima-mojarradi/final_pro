from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from .authentication import create_access_token, create_refresh_token,decode_access_token,decode_refresh_token
from rest_framework.exceptions import APIException
from .models import CustomUser
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@csrf_protect
class LoginUserView(CreateAPIView):
    def post(self,request):
        user = CustomUser.objects.filter(username=request.data['username']).first()
        if not user:
            raise APIException('invalid credential')
        
        if not user.check_password(request.data['password']):
            raise APIException('invalid credential!')        
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)
        response = Response()
        response.set_cookie(key='refresh_token',value=refresh_token, httponly=True)
        response.data = {
            'access_token':access_token
        }
        return response
    
class UserAPIView(APIView):
    def get(self,request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = CustomUser.objects.filter(pk=id).first()

            return Response(UserSerializer(user).data)
        else:
            raise AuthenticationFailed('unauthenticated')


