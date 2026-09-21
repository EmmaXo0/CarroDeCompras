from datetime import datetime

def generar_ticket(carrito, catalogo, total):
   
    folio = f"F{datetime.now().strftime('%Y%m%d%H%M%S')}"
    fecha = datetime.now().strftime('%Y-%m-%d')
    
    print("\n" + "="*30)
    print(f" TICKET DE VENTA - {folio}")
    print(f" Fecha: {fecha}")
    print("="*30)
    for id_prod, cant in carrito:
        nombre = catalogo[id_prod]["nombre"]
        precio = catalogo[id_prod]["precio"]
        print(f"{nombre} x{cant} - ${precio * cant:.2f}")
    print("-" * 30)
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("="*30)
   
    return (folio, fecha, total)
