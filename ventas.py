def calcularImporte(precio, cantidad):
    """Calcula el importe de una linea de compra."""
    importe = precio * cantidad
    return round(importe, 2)


def calcularTotal(subtotal, descuento=0.0, impuesto=0.16):
    """Aplica descuento e impuesto al subtotal y devuelve total redondeado a 2 decimales."""
    monto_descuento = subtotal * descuento
    subtotal_con_descuento = subtotal - monto_descuento
    monto_impuesto = subtotal_con_descuento * impuesto
    total = subtotal_con_descuento + monto_impuesto
    return round(total, 2)


def aplicarCuponGame50(subtotal, codigo_cupon):
    """Punto extra: descuenta $50.00 si el cupon es GAME50 (sin bajar de 0)."""
    if codigo_cupon.strip().upper() == "GAME50":
        nuevo_subtotal = subtotal - 50.00
        if nuevo_subtotal < 0:
            nuevo_subtotal = 0.0
        return round(nuevo_subtotal, 2)
    return round(subtotal, 2)