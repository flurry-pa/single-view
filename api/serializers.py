from rest_framework import serializers

from sv.models import Author, MusicWork


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class MusicWorkSerializer(serializers.ModelSerializer):
    author_names = serializers.SerializerMethodField()

    class Meta:
        model = MusicWork
        fields = ('id', 'title', 'iswc', 'author_names')

    def get_author_names(self, obj):
        return {author.pk: author.name for author in obj.authors.all()}
