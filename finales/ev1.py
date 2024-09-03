MONTO_IRP = 80000000  # Monto a partir del cual se deben pagar impuestos

try:
    sueldo = int(input("Ingrese cuál es su sueldo mensual: "))
    
    sueldo_anual = sueldo * 12  # Calcula el sueldo anual
    
    if sueldo_anual > MONTO_IRP:
        print(f"Esta persona debe pagar impuestos. Su sueldo anual es: {sueldo_anual} Gs.")
    else:
        print(f"Esta persona no debe abonar impuestos. Su sueldo anual es: {sueldo_anual} Gs.")
        
except ValueError:
    print("Error: Por favor ingrese un número válido para el sueldo.")
