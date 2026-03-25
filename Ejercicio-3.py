el_nombre_tiene_error = True
while el_nombre_tiene_error == True:
    print("Ingrese el nombre del producto que va a comprar: ")
    nombre_del_producto = input()
    if nombre_del_producto == "": #Solución al BUG número 1
        print("ERROR: El nombre del producto no puede ser vacio")
    else:
        el_nombre_tiene_error = False
#output
print("Ingrese el precio del producto que va a comprar: ")
#input + variable
precio_del_producto = input()
if precio_del_producto == "": #Solución al BUG número 2
    print("ERROR: El precio del producto no puede ser vacío")
else:
    precio_del_producto = float(precio_del_producto)
    if precio_del_producto < 0: #Solución al BUG número 5
        print("ERROR: El precio del producto no puede ser negativo")
    else:
        #output
        print("Ingrese el valor del descuento del producto: ")
        #input + variable
        descuento = input()
        if descuento == "": #Solución al BUG número 6
            descuento = "0"

        descuento = float(descuento)

        if descuento < 0: #Solucíon al BUG número 7
            print("ERROR: El descuento no puede ser un valor negativo")
        else:
            if precio_del_producto < descuento: #Solución al BUG número 8
                print("ERROR: El descuento no puede superar el valor del producto")
            else:
                precio_final_del_producto = precio_del_producto - descuento

                #output
                print(f"El producto que quiere comprar se llama: {nombre_del_producto} y tiene un precio de: {precio_final_del_producto}")