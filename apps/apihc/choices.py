

def ERRCLI_CODES(fieldData, catalogo, catalogo2):
    errors = {
        "ERRCLI-001": f"{fieldData} no se encuentra en el catálogo {catalogo}",
        "ERRCLI-002": f"{fieldData} del catálogo {catalogo} no se relaciona con el catálogo {catalogo2}"
    }

    return errors