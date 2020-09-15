from django.conf.urls import url
from django.urls import include

from api.routers import router

app_name = 'sv'
urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
