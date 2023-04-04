from jwt import encode, decode

def create_token(data: dict):
    token = encode(payload=data, key="my_ultra_secrete_key", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
  data: dict = decode(token, key='my_ultra_secret_key', algorithms=['HS256'])
  return data