import jwt
key = 'secret'
token = jwt.encode({'payload': 'abc123'}, key, 'HS256')
print(token)

print(jwt.decode(token, key, algorithms=))

