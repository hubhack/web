# from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, JsonResponse, HttpResponse
import simplejson
from .models import User
import datetime
import jwt
import bcrypt
from django.conf import settings
def gen_token(user_id):
    return jwt.encode({
        'user_id':user_id,
        'timestamp':int(datetime.datetime.now().timestamp())# 取整

    }, settings.SECRET_KEY).decode()
# 用户注册
def reg(request:HttpRequest):
    try:
        payload = simplejson.loads(request.body)
        email = payload['email']
        query = User.objects.filter(email=email)
        print('-------', query)
        print(query)
        print(query.query)
        if query.first():
            return JsonResponse({'error':'用户已存在'}, status=400)
        name = payload['name']
        password = payload['password'].encode()
        print(email, name, password)
        password = bcrypt.hashpw(password, bcrypt.gensalt())
        print(password)
        # 数据库导入
        user = User()
        user.email = email
        user.name = name
        user.password = password.decode() # 转成字符串
        user.save()
        return JsonResponse({'token':gen_token(user.id)}, status = 201)
    except Exception as e:
        print(e)
        # 失败返回错误信息和404, 所有其他错误一律用户名密码错误
        return JsonResponse({'error': '用户名和密码错误'}, status=400)
# 用户登录
def login(request:HttpRequest):
    try:
        payload = simplejson.loads(request.body)
        email = payload['email']
        password = payload['password'].encode()
        user = User.objects.get(email=email)
        if bcrypt.checkpw(password, user.password.encode()):
            token = gen_token(user.id)
            return JsonResponse({'token':token}, status=201)
        else:
            return JsonResponse({'error'},status=400)
    except Exception as e:
        return JsonResponse({'error'},status=400)



# def authenticate(viewfunc):
#     def wrapper(*args):
#         print(1, '-' * 30)
#         *s, request = args
#
#
#         # 认证,越早越好

