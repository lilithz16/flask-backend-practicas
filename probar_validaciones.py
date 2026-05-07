from services.validation_service import validar_datos_candidato, normalizar_telefono


datos_candidato = {
    "nombre": "Lidia",
    "apellidos": "Martín Ayuso",
    "email": "lidia@gmail.com",
    "telefono": "+34 600 123 123",
    "puesto": "Programadora",
    "privacidad": "true"
}

es_valido, mensaje = validar_datos_candidato(datos_candidato)

print("Resultado de validación:")
print(es_valido)
print(mensaje)

print("Teléfono normalizado:")
print(normalizar_telefono(datos_candidato.get("telefono")))