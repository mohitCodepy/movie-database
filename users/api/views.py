from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from users.api.serializers import UserSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    http_method_names = ['get', 'post']
    queryset = User.objects.all()
    serializer_class = UserSerializer
