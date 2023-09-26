import hashlib

#cifrado
def cifrar_rot_n(texto, n):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            offset = 65 if caracter.isupper() else 97  # Asegurar que estamos trabajando con letras mayúsculas o minúsculas
            resultado += chr((ord(caracter) - offset + n) % 26 + offset)
        else:
            resultado += caracter
    return resultado


# Leer el mensaje de entrada desde el archivo
with open('mensajedeentrada.txt', 'r') as archivo_entrada:
    mensaje = archivo_entrada.read()

# Cifrar el mensaje usando ROT(n)
n = 3  
mensaje_cifrado = cifrar_rot_n(mensaje, n)

#hash mensaje original
hash_obj = hashlib.sha256()
menBytes = mensaje.encode('utf-8')
hash_obj.update(menBytes)
hash_resultante = hash_obj.hexdigest()

seguro = (f"{mensaje_cifrado}\n"+f"{hash_resultante}")

# Guardar el mensaje cifrado en un archivo
with open('mensajeseguro.txt', 'w') as archivo_salida:
    archivo_salida.write(seguro)

print(f"Archivo escrito exitosamente\n", 
      seguro)