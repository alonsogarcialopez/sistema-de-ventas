from inventario import (
    crearCatalogo,
    mostrarCatalogo,
    buscarProducto,
    hayExistencia,
    actualizarExistencia
)
from ventas import (
    calcularImporte,
    calcularTotal,
    aplicarCuponGame50
)


def main():
    """Controla el flujo general del programa."""
    catalogo = crearCatalogo()
    carrito = []

    mostrarCatalogo(catalogo)

    while True:
        codigo = input("\nIngresa el codigo del videojuego (o escribe SALIR para terminar): ").strip()
        if codigo.upper() == "SALIR":
            break

        producto = buscarProducto(catalogo, codigo)
        if producto is None:
            print("El codigo ingresado no existe. Intenta de nuevo.")
            continue

        texto_cantidad = input("Ingresa la cantidad que deseas comprar: ").strip()
        if not texto_cantidad.isdigit():
            print("Ingresa un numero entero valido.")
            continue

        cantidad = int(texto_cantidad)
        if not hayExistencia(producto["existencia"], cantidad):
            if cantidad <= 0:
                print("Cantidad no valida. Debe ser mayor a 0.")
            else:
                print(f"Existencia insuficiente. Solo hay {producto['existencia']} unidades disponibles.")
            continue

        importe = calcularImporte(precio=producto["precio"], cantidad=cantidad)
        producto["existencia"] = actualizarExistencia(existencia=producto["existencia"], cantidad=cantidad)

        linea = {
            "codigo": producto["codigo"],
            "nombre": producto["nombre"],
            "cantidad": cantidad,
            "importe": importe
        }
        carrito = carrito + [linea]
        print(f"Agregado: {cantidad} x {producto['nombre']} -> Importe: ${importe}")

  
    print("\n=== RESUMEN DE COMPRA ===")
    subtotal = 0.0
    for item in carrito:
        print(f"{item['codigo']} - {item['nombre']} | Cantidad: {item['cantidad']} | Importe: ${item['importe']}")
        subtotal = subtotal + item["importe"]

    subtotal = round(subtotal, 2)

    if subtotal >= 1000.00:
        porcentaje_descuento = 0.10
    else:
        porcentaje_descuento = 0.0

    cupon = input("\nTienes cupon de descuento? (Escribe GAME50 o presiona Enter): ").strip()
    subtotal_tras_cupon = aplicarCuponGame50(subtotal, cupon)

    monto_descuento_regla = round(subtotal_tras_cupon * porcentaje_descuento, 2)
    total_pagar = calcularTotal(subtotal_tras_cupon, descuento=porcentaje_descuento, impuesto=0.16)
    monto_impuesto = round(total_pagar - (subtotal_tras_cupon - monto_descuento_regla), 2)

    print(f"Subtotal inicial: ${subtotal}")
    if cupon.upper() == "GAME50":
        print(f"Subtotal tras cupon GAME50 (-$50.00): ${subtotal_tras_cupon}")
    print(f"Descuento aplicado ({int(porcentaje_descuento * 100)}%): ${monto_descuento_regla}")
    print(f"Impuesto (16%): ${monto_impuesto}")
    print(f"TOTAL A PAGAR: ${total_pagar}")

    
    print("\n=== INVENTARIO RESTANTE ===")
    for prod in catalogo:
        print(f"{prod['codigo']} - {prod['nombre']}: {prod['existencia']} unidades")


if __name__ == "__main__":
    main()