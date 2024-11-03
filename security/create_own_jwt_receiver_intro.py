import jwt

headers = {
    'alg': 'HS256', 
    'type': 'Jwt',
}

payload = {
    'username': 'tester1',
    'email': 'testemailgmail.com',
    'isactive': False,
}

secret = 'secret123' # Це просто приклад ключа на діллі потім розглянемо більш правельний варіант

encode_token = jwt.encode(headers=headers, payload=payload, key=secret)
print(encode_token)

try:
    decoded_token = jwt.decode(encode_token, secret, algorithms='HS256')
    print(decoded_token)
except jwt.InvalidTokenError:
    print('Invalid token')
except jwt.DecodeError:
    print('Decode error')   