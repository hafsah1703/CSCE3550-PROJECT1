from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import time

keys = {}

def generate_key(kid):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    serialized_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    serialized_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    keys[kid] = {
        'private': serialized_private,
        'public': serialized_public,
        'expiry': int(time.time()) + 3600  # 1 hour expiry
    }
    return serialized_public

def get_key(kid):
    if kid in keys and keys[kid]['expiry'] > int(time.time()):
        return keys[kid]['public']
    return None
