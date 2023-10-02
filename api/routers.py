from rest_framework import routers

from api.viewsets import AuthorViewSet, MusicWorkViewSet

router = routers.SimpleRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'music_works', MusicWorkViewSet)
