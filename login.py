
import time 
import getpass 

# Sistema de login básico
usuarios = {"usuario1": "contraseña1", "usuario2": "contraseña2"}

def login(usuario, password):
    if usuario in usuarios and usuarios[usuario] == password:
         return True
    else:
        return False
    
def convertir_a_binario(texto):
    return ''.join(format(ord(char), '08b') for char in texto)

 

def login_con_binario(usuario, password):
    if login(usuario, password):
        contraseña_binaria = convertir_a_binario(password)
        return True, print (f"Login exitoso y la contraseña binaria es: \n {contraseña_binaria}")
    else:
       return False, print("Login fallido")


def convertir_numero_a_binario(numero):
    return format(numero, '08b')

def obtener_hora_binaria():
    hora_actual = time.localtime()
    hora_binaria = convertir_numero_a_binario(hora_actual.tm_hour)
    minuto_binario = convertir_numero_a_binario(hora_actual.tm_min)
    segundo_binario = convertir_numero_a_binario(hora_actual.tm_sec)
    return hora_actual,hora_binaria, minuto_binario, segundo_binario 

# Prueba de login con binario
print ("================================= \n")
print("Sistema de login \n")
print ("================================= \n")

print("Ingrese sus credenciales \n")

usuario = input("Nombre de usuario: ")

password = getpass.getpass("Contraseña: ")

print ("================================= \n")
valido,mensaje = login_con_binario(usuario, password)
hora_actual,hora_binaria, minuto_binario, segundo_binario = obtener_hora_binaria()
if(valido):
    print ("================================= \n")
    
   
    print(f"Hora de acceso: {hora_actual.tm_hour}:{hora_actual.tm_min}:{hora_actual.tm_sec}   ,hora: {hora_binaria}, Minuto: {minuto_binario}, Segundo: {segundo_binario}")
    print ("================================= \n")
    print("Acceso concedido \n") 
    print ("================================= \n")

else:
    print ("================================= \n")
    
    print ("Acceso denegado \n")
    print ("================================= \n")


