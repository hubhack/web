from django.conf.urls import url
from .views import PostView, getpost
# from user.views import authenticate
urlpatterns = [
    url(r'^$', PostView.as_view()), # /posts/视图类PostViews
    url(r'(\d+)$', getpost),
]