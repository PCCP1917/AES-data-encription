from cryptography.fernet import Fernet

def generar_clave():
    return Fernet.generate_key()

def encriptar_texto(texto , clave):
    f= Fernet(clave)
    texto_encriptado= f.encrypt(texto.encode())
    return texto_encriptado

def desencriptar_texto(texto , clave):
    f= Fernet(clave)
    texto_desencriptado= f.decrypt(texto.decode())
    return texto_desencriptado

#Generar clave secreta
Clave_Secreta = generar_clave()

#Introducir texto a encriptar 
Mensaje= input("Ingrese un mensaje de encripción: \n")

#Mostrar Texto Encriptado
Mensaje_Encriptado=encriptar_texto(Mensaje,Clave_Secreta)
print('*'*20)
print("Mensaje Encriptado: \n")
print(Mensaje_Encriptado)

#Mostrar Clave de encripcion
print('*'*20)
print("Clave Secreta: \n")
print(Clave_Secreta)

#Mostrar texto desencriptado
Mensaje_desencriptado=desencriptar_texto(Mensaje_Encriptado,Clave_Secreta)
print('*'*20)
print(f"Mensaje Desencriptado: \n{Mensaje_desencriptado}")