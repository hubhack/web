from django.conf.urls import url
from .views import reg,login
urlpatterns = [
    url(r'^$', reg), # /users/
    # url(r'^test$', test),
    url(r'^login$', login)

]