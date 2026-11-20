def crearCatalogo():
    """Crea y devuelve el catalogo inicial de videojuegos."""
    catalogo = [
        {"codigo": "G001", "nombre": "Cyberpunk 2077", "precio": 699.00, "existencia": 5},
        {"codigo": "G002", "nombre": "Minecraft", "precio": 499.00, "existencia": 8},
        {"codigo": "G003", "nombre": "Grand Theft Auto VI", "precio": 1199.00, "existencia": 3},
        {"codigo": "G004", "nombre": "FC27", "precio": 999.00, "existencia": 4},
        {"codigo": "G005", "nombre": "Mario Kart", "precio": 249.00, "existencia": 10}
    ]
    return catalogo


def mostrarCatalogo(catalogo):
    """Muestra todos los productos y sus existencias."""
    print("\n--- CATALOGO DE TIENDA GAMEZONE ---")
    for prod in catalogo:
        print(f"Codigo: {prod['codigo']} | {prod['nombre']} | Precio: ${round(prod['precio'], 2)} | Existencia: {prod['existencia']}")


def buscarProducto(catalogo, codigo):
    """Localiza un producto por su codigo. Devuelve el diccionario o None."""
    codigo_buscado = codigo.strip().upper()
    for prod in catalogo:
        if prod["codigo"] == codigo_buscado:
            return prod
    return None


def hayExistencia(existencia, cantidad):
    """Valida que la cantidad solicitada este disponible y sea valida."""
    if cantidad <= 0:
        return False
    if cantidad > existencia:
        return False
    return True


def actualizarExistencia(existencia, cantidad):
    """Calcula las unidades restantes despues de una venta valida."""
    restante = existencia - cantidad
    return restante