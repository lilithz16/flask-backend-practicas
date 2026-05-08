EXTENSIONES_PERMITIDAS = ["pdf", "doc", "docx"]


def extension_permitida(nombre_archivo):
    if nombre_archivo is None:
        return False

    if nombre_archivo.strip() == "":
        return False

    if "." not in nombre_archivo:
        return False

    extension = nombre_archivo.rsplit(".", 1)[1].lower()

    return extension in EXTENSIONES_PERMITIDAS