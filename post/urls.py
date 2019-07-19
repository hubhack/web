from django.conf.urls import url
from .views import PostView, getpost

urlpatterns = [
    url(r'^$', PostView.as_view()),
    url(r'(\d+)$', getpost),
]