from rest_framework import serializers

from sv.models import Author, MusicWork


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class MusicWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicWork
        fields = '__all__'
