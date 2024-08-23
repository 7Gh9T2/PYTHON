usuarios = {
    "Luana": "123",
    "lili" : "000",
    "Caty": "2828",
 }

intentos = 0

while intentos < 3:
    usuario = input("Ingresa tu usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Acceso concedido.")
        break
    else:
        print("Usuario o contraseña incorrectos.")
        intentos += 1

if intentos == 3:
    print("Acceso denegado, demasiados intentos.")
