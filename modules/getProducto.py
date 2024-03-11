import storage.producto as pr
# Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales
# y que tienen mas de 100 unidades en stock. El listado debera estar ordenado por su precio de venta,
# mostrando en primerm lugar los de mayor precio.

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in pr.producto:
        if(val.get("gama") == gama and val.get("precio_venta") >= stock):
            condiciones.append(val)

    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price)

    return condiciones