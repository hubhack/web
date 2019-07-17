from django.test import TestCase

# Create your tests here.

import datetime
import jwt
import bcrypt
import simplejson
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.conf import settings

from django.views.decorators.http import require_http_methods, require_POST
from .models import User

AUTH_EXPIRE = 8 * 60 * 60
AUTH_HEADER = "HTTP_JWT"
def gen_token(user_id):
    return jwt.encode({
        'user_id':user_id,
        'exp':int(datetime.datetime.now().timestamp()) + AUTH_EXPIRE# 取整

    }, settings.SECRET_KEY).decode()


# 用户注册
@require_http_methods(['POST'])
def reg(request:HttpRequest):
    try:
        payload = simplejson.loads(request.body)
        email = payload['email']
        query = User.object.filter(email=email)
        print(query)
        print(query.query)
        if query.first():
            return JsonResponse({'error': '用户已存在'}, status=400)
        name = payload['name']
        password = payload['password'].encode()
        print(email, name, password)
        password = bcrypt.hashpw(password, bcrypt.gensalt())
        print(password)

        user = User()
        user.email = email
        user.name = name
        user.password = password.decode()
        user.save()
        return JsonResponse({'token':gen_token(user.id)}, status=201)
    except Exception as e:
        print(e)
        return JsonResponse({'error': '用户名或密码错误'}, status =400)

def jsonify(instance, allow=None, exclude=[]):
    modecls = type(instance)
    if allow:
        fn = (lambda x: x.name in allow)
    else:
        fn = (lambda x : x.name not in exclude)

    return {k.name:getattr(instance, k.name) for k in filter(fn, modecls._meta.fields)}


@require_POST
def login(request):
    try:
        payload = simplejson.loads(request.body)

        print(payload)
        email = payload['email']
        password = payload['password'].encode()
        print(email, password)

        user = User.objects.get(email=email) # only one
        print(user.password)

        if bcrypt.checkpw(password, user.password.encode()):
            token = gen_token(user.id)
            res = JsonResponse({
                'user':jsonify(user, exclude=['password']),
                'token': token

            })# 返回200

            res.set_cookie('jwt', token)
            return res
        else:
            return JsonResponse({'error': "用户名或密码错误"}, status=400)

    except Exception as e:
        print(e)
        return JsonResponse({'error': "用户名或密码错误"}, status=400)

def authenticate(viewfunc):
    def wrapper(request:HttpRequest):
        print(1, '-' * 30)
        jwtheader = request.META.get(AUTH_HEADER, '')
        if not jwtheader:
            return HttpResponse(status=401)
        print(jwtheader)

        try:
            payload = jwt.decode(jwtheader, settings.SECRET_KEY,
                                 algorithms=['HS256'],
                                 options={'verify_signature':True})
            print(payload)
        except Exception as e:
            return HttpResponse(status=401)
        print('-' * 30)
        try:
            user_id = payload.get('user_id', 0)
            if user_id == 0:
                return HttpResponse(status=401)
        response = viewfunc(request)
        return response
    return wrapper
@require_POST
@authenticate
def test(request):
    print(request.user)
    return JsonResponse({}, status=200)