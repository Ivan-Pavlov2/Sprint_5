import random
import string

def generate_login():
    characters = string.ascii_lowercase
    login = ''.join(random.choice(characters) for _ in range(8))
    return login

def generate_password():
    characters = string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(8))
    return password
