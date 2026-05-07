import re


def campo_obligatorio(valor):
    if valor is None:
        return False

    if str(valor).strip() == "":
        return False

    return True


def email_valido(email):
    if not campo_obligatorio(email):
        return False

    email = email.strip().lower()

    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    return re.match(patron, email) is not None


def normalizar_telefono(telefono):
    if telefono is None:
        return None

    telefono = telefono.strip()
    telefono = telefono.replace(" ", "")
    telefono = telefono.replace("-", "")

    if telefono.startswith("+34"):
        telefono = telefono[3:]

    if telefono.startswith("0034"):
        telefono = telefono[4:]

    return telefono


def telefono_valido(telefono):
    telefono = normalizar_telefono(telefono)

    if not campo_obligatorio(telefono):
        return False

    patron = r"^[6789][0-9]{8}$"

    return re.match(patron, telefono) is not None


def privacidad_valida(valor):
    valores_validos = ["true", "on", "1", True]

    return valor in valores_validos


def validar_datos_candidato(datos):
    validaciones = [
        (campo_obligatorio(datos.get("nombre")), "El nombre es obligatorio."),
        (campo_obligatorio(datos.get("apellidos")), "Los apellidos son obligatorios."),
        (email_valido(datos.get("email")), "El email no es válido."),
        (telefono_valido(datos.get("telefono")), "El teléfono no es válido."),
        (campo_obligatorio(datos.get("puesto")), "El puesto solicitado es obligatorio."),
        (privacidad_valida(datos.get("privacidad")), "Debe aceptar la política de privacidad.")
    ]

    for condicion, mensaje_error in validaciones:
        if not condicion:
            return False, mensaje_error

    return True, "Datos válidos."