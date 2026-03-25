#output
print ("ingrese el nombre del producto que va a comprar: ")
#input + variable
nombre_del_producto = input()

#output
print ("Ingrese el precio del producto que va acomprar: ")
precio_del_producto = input()
precio_del_producto = float(precio_del_producto)

#output
print ("Ingrese el valor de descuento del producto: ")
descuento = input()
descuento = float(descuento)

precio_final_del_producto = precio_del_producto - descuento

print (f"El producto que quiere comprar se llama: {nombre_del_producto} y tiene un precio de: {precio_final_del_producto}")
