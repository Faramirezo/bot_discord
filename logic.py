import random as r, string as s
def contra(largo):
    elements = s.ascii_letters+s.ascii_lowercase+s.ascii_uppercase+s.digits+s.punctuation
    password = ''
    for i in range(largo):
        password += r.choice(elements)
    return password

def coin():
    caras= ["cara", "cruz"]
    seleccion= r.choice(caras)
    return seleccion