def suma(a: int, b: int) -> int:
    """Retorna la suma de dos números."""
    return a + b

def longitud(texto: str) -> int:
    """Retorna la cantidad de caracteres de una cadena."""
    return len(texto)

def es_par(numero: int) -> bool:
    """Verifica si un número entero es par."""
    return numero % 2 == 0

def repetir_texto(texto: str, veces: int) -> str:
    """Repite un texto una cantidad específica de veces."""
    return texto * veces