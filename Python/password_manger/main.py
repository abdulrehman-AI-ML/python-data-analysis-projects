import random 
import string

password = {}

try:
    with open('file.txt','r') as f:
        for line in f:
            website,pwd = line.strip().spilt(":")
            password[website] = pwd 
except:
    pass

def genrate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

