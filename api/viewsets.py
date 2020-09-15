from rest_framework.viewsets import ModelViewSet

from api.serializers import AuthorSerializer, MusicWorkSerializer
from sv.models import Author, MusicWork


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class MusicWorkViewSet(ModelViewSet):
    serializer_class = MusicWorkSerializer
    queryset = MusicWork.objects.all()
