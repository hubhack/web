import bcrypt


password = b'12233'
x = bcrypt.hashpw(password, bcrypt.gensalt())
print(x)
print(bcrypt.checkpw(password, x))