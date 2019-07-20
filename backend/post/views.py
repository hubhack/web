from django.shortcuts import render

# Create your views here.

import datetime
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from django.views import View
from .models import Post, Content
from user.models import User
import simplejson
# from utils import jsonify
# from user.views import authenticate


class PostView(View):# 增加
    def get(self, request:HttpRequest):
        print('get--------')

    def post(self, request:HttpRequest):
        print('post----------------')
        post = Post()
        content = Content()
        try:
            payload = simplejson.loads(request.body)
            post.title = payload['title']
            post.author = User(id=request.user.id)
            post.postdate = datetime.datetime.now(
                datetime.timezone(datetime.timedelta(hours=8))
            )
            post.save()


            content.post =post
            content.content = payload['content']


            content.save()
            return JsonResponse({
                # 'post': jsonify(post, allow['id', 'title'])
            })
        except Exception as e:
            print(e)
            return HttpResponse(status=400)


def getpost(request:HttpRequest, id):
    print(id)
    return JsonResponse({}, status=201)

