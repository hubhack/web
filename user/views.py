# from django.shortcuts import render

# Create your views here.

from django.http import  HttpRequest, HttpResponse, JsonResponse, Http404
import simplejson
import logging
FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format = FORMAT, level=logging.INFO)
from .models import User
from django.db.models import Q
import bcrypt


def reg(request: HttpRequest): # POST
    print(1, request.GET)
    print(2, request.POST)
    print(3, request.body)
    print(4, request.content_type)
    try:
        payload = simplejson.loads(request.body)
        print(type(payload), payload)
        email = payload['email']
        query = User.objects.filter(email=email).first()

        if query:
            return JsonResponse({'error':'该用户已存在'}, status=400)


        name = payload['name']
        password = payload['password']
        print(email, name, password)

        user = User()
        user.name = name
        user.email = email
        user.password = password

        user.save() # save 会自动事务提交



        return JsonResponse({}, status=201)
    except Exception as e:
        logging.error(e)
        return JsonResponse ({'error': '用户输入错误'}, status=400)

def test(request):
    # user = User.objects.filter(email='abc') # 太懒
    email = '123@qq.com'
    # qs = User.objects.filter(email='123@qq.com').all()
    # TODO 测试
    mgr = User.objects
    qs = mgr.filter(Q(pk__lt=6))
    print('*********',qs,'-----------')
    # print('^^^^^^', *qs)
    return JsonResponse ({'test':"ok"})


def login(request):
    try:
        payload = simplejson.loads(request.body)
        print(payload)
        email = payload['email']
        password = payload['passsword'].encode()
        print(email, password)

        user = User.object.get(email=email)
        print(user.password)
        if bcrypt.checkpw(password, user.password.encode()):
            # 验证成功
            token = gen_token(user.id)
            res = JsonResponse({
                'user':jsonify(user, exclude=['password']),
                'token':token
            })
            res.set_cookie('jwt', token)
            return res
        else:
            return JsonResponse({'error':'用户名或密码错误'}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({'error': '用户名或密码错误'}, status=400)

def jsonify(instance, allow=None, exclude=[]):
    modelcls = type(instance)
    if allow:
        fn = (lambda x: x.name in allow)
    else:
        fn = (lambda x: x.name not in exclude)