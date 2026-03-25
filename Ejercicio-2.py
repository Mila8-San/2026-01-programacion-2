print ("ingrese el nombre del producto que va a comprar: ")
nombre_del_producto = input()
if nombre_del_producto == "":
    print ("ERROR: El nombre del producto no puede estar vacio")
else:
    print ("Ingrese el precio del producto que va acomprar: ")
    precio_del_producto = input()
    if precio_del_producto == "":
        print ("ERROR: El precio del producto no puede estar vacio")
    else:
        precio_del_producto = float(precio_del_producto)
        if precio_del_producto < 0:
            print ("ERROR: El precio del producto no puede ser negativo")
        else:
            print ("Ingrese el valor de descuento del producto: ")
            descuento = input()
            if descuento == "":
                descuento= "0"
            
            descuento = float(descuento)

            if descuento <0:
                print ("ERROR: El descuento no puede ser un valor negativo")
            else:
                if precio_del_producto < descuento:
                    print ("ERROR: El descuento no puede superar el valor del producto")
                else:
                    precio_final_del_producto = precio_del_producto - descuento

                    print (f"El producto que quiere comprar se llama: {nombre_del_producto} y tiene un precio de: {precio_final_del_producto}")
