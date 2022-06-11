from passlib.hash import pbkdf2_sha256 

def hash_password(password):
    return pbkdf2_sha256.hash(password)


def compare_password(hash,password):
    pbkdf2_sha256.verify(password,hash)

