import hashlib

def cifrar_rot_n(texto, n):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            offset = 65 if caracter.isupper() else 97  # Asegurar que estamos trabajando con letras mayúsculas o minúsculas
            resultado += chr((ord(caracter) - offset + n) % 26 + offset)
        else:
            resultado += caracter
    return resultado

def descifrar_rot_n(texto, n):
    return cifrar_rot_n(texto, -n)

# Leer el mensaje cifrado y el hash desde el archivo seguro
with open('mensajeseguro.txt', 'r') as archivo_seguro:
    lineas = archivo_seguro.readlines()
    mensaje_cifrado_guardado = lineas[0].strip()
    hash_guardado = lineas[1].strip()

# Descifrar el mensaje cifrado usando el mismo valor de n
n = 3  # Debes usar el mismo valor de n que se usó para cifrar
mensaje_descifrado = descifrar_rot_n(mensaje_cifrado_guardado, n)

# Calcular el hash del mensaje descifrado
hash_obj = hashlib.sha256()
mensaje_descifrado_bytes = mensaje_descifrado.encode('utf-8')
hash_obj.update(mensaje_descifrado_bytes)
hash_calculado = hash_obj.hexdigest()

# Verificar la integridad del mensaje
if hash_calculado == hash_guardado:
    print("Integridad del mensaje verificada: El mensaje no ha sido modificado.")
else:
    print("Integridad del mensaje no verificada: El mensaje ha sido modificado.")

# Imprimir el mensaje descifrado
print("Mensaje descifrado:", mensaje_descifrado)

with open('mensajesDescifrado.txt', 'w') as archivo_salida:archivo_salida.write(f"{mensaje_descifrado}\n" +f"{hash_calculado}")

print(f"Archivo escrito exitosamente\n")