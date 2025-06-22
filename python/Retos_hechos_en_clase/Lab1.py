#listas para guardar información de cada libro
libros = []
subtotal = 0
descuento_academico_total = 0
descuento_afiliacion_total = 0

#solicitar cantidad
cantidad = int(input("\n¿Cuántos libros desea comprar? "))

#datos por cada libro
for i in range(1, cantidad + 1):
    print(f"\nLibro #{i}")
    precio = float(input("Precio del libro: $"))
    es_academico = input("¿Es un libro académico? (s/n): ").lower() == 's'
    es_afiliado = input("¿El comprador está afiliado a ULagos? (s/n): ").lower() == 's'
    
    #subtotal general
    subtotal += precio

    #descuento A: académico
    desc_acad = precio * 0.15 if es_academico else 0
    precio_con_desc_acad = precio - desc_acad

    #descuento B: afiliación
    desc_afiliado = precio_con_desc_acad * 0.05 if es_afiliado else 0
    precio_final_individual = precio_con_desc_acad - desc_afiliado

    #guardar descuentos individuales
    descuento_academico_total += desc_acad
    descuento_afiliacion_total += desc_afiliado

    #guardar información por libro
    libros.append({
        "Precio original": precio,
        "Académico": es_academico,
        "Afiliado": es_afiliado,
        "Descuento académico": desc_acad,
        "Descuento afiliación": desc_afiliado,
        "Precio final libro": precio_final_individual
    })

#sumar total después de descuentos A y B
total_sin_volumen = sum(libro["Precio final libro"] for libro in libros)

#descuento C: volumen si total supera $50.000
descuento_volumen = total_sin_volumen * 0.05 if total_sin_volumen > 50000 else 0
total_final = total_sin_volumen - descuento_volumen

#mostrar desglose general
print("\n========== DESGLOSE GENERAL ==========")
print(f"Subtotal sin descuentos: ${subtotal:,.0f}")
print(f"Descuento total por libros académicos: ${descuento_academico_total:,.0f}")
print(f"Descuento total por afiliación ULagos: ${descuento_afiliacion_total:,.0f}")
print(f"Descuento por volumen de compra: ${descuento_volumen:,.0f}")
print(f"Descuento total acumulado: ${descuento_academico_total + descuento_afiliacion_total + descuento_volumen:,.0f}")
print(f"Total a pagar: ${total_final:,.0f}")

#mostrar desglose por libro
print("\n========== DETALLE POR LIBRO ==========")
for i, libro in enumerate(libros, start=1):
    print(f"\nLibro #{i}")
    print(f"Precio original: ${libro['Precio original']:,.0f}")
    print(f"Académico: {'Sí' if libro['Académico'] else 'No'}")
    print(f"Afiliado ULagos: {'Sí' if libro['Afiliado'] else 'No'}")
    print(f"Descuento académico: ${libro['Descuento académico']:,.0f}")
    print(f"Descuento afiliación: ${libro['Descuento afiliación']:,.0f}")
    print(f"Precio final después de descuentos: ${libro['Precio final libro']:,.0f}")