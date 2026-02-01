import re

def contraseña_segura(password):
    if (len(password) >= 6 and
        re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password)):
        return True
    return False
