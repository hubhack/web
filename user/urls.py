from django.conf.urls import url
from .views import reg,test

urlpatterns = [
    url(r'^$', reg), # /users/
    url(r'^test$', test)
]