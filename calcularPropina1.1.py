#--------------------------------CALCULADORA DE PROPINAS------------------------------
# version 1.1
# en esta version me centre en que funcionase todos los menus (creando nuevas funciones) 
# y por lo tanto que funcionase toda el programa sin bugs obviando claro el manejo de 
# exepciones que lo solucionare en una version posterior ademas de limpieza de codigo.
import re
    #PENDIENTE:
    #MANEJO DE EXEPCIONES PARA CADA MENU
    #LIMPIEZA DEL CODIGO    

def tomadelafacturaOriginal():
    factura1 = input("porfavor ingrese la factura total de hoy: ")
    print(f"este es el valor de la factura de hoy: {factura1}")
    verificador = int(input(f"""---------------------------------------------------------------------
estas seguro que este fue el valor de la factura?: 
1. confirmar
2. rechazar
-------------------------------------------------------------------------
            : """))
    if verificador == 1:
        return factura1
    else:
        print("VUELVE A INTENTARLO")
        factura1 = tomadelafacturaOriginal()
        return factura1

def escojerDivisa():
    divisaEscojida = input("""que divisa estas manejando en esta factura?: 
1. USD (dolares estadounidenses)
2. COP (pesos colombianos)
                           """)
    if divisaEscojida == "2":
        return divisaEscojida
    elif divisaEscojida == "1":
        return divisaEscojida
         
def eliminandoCaracteresInnecesarios(divisa, valorList):
    pattern =r"\w[a-zA-Z]+\s+"
    new_text = re.sub(pattern, "", valorList)     
    #print("Texto modificado:", new_text)
    valorList = list(new_text)
    if divisa == "2":
        analphabeticList1 = ["m","y","."," ","","$",",","-",":", ";", "!", "?", "'", "\""] 
        for character in analphabeticList1: 
            while character in valorList: 
                valorList.remove(character)
        return valorList
    elif divisa == "1":
        analphabeticList = ["m","y"," ","","$",",","-", ":", ";", "!", "?", "'", "\""]
        for character in analphabeticList: 
            if character in valorList: 
                valorList.remove(character) 
        return valorList
            
def calculandoPropina(valorConPropina):
    while True:
        porcentaje_propina = input("""----------------------------------------------------
ahora escoje el porcentaje de propina que quieres aplicar
a la factura:
1. para el 18%
2. para el 20%
3. para el 25%
4. Para ingresar un porcentaje manualmente
            : """)
        valorConPropina = float(''.join(valorConPropina))
        if porcentaje_propina == "1":
            valorConPropina = ((valorConPropina * 0.18) + valorConPropina)
            return valorConPropina
        elif porcentaje_propina == "2":
            valorConPropina = ((valorConPropina * 0.20) + valorConPropina)
            return valorConPropina
        elif porcentaje_propina == "3":
            valorConPropina = ((valorConPropina * 0.25) + valorConPropina)
            return valorConPropina
        elif porcentaje_propina == "4":
            while True:
                try:
                    porcentajeManual = int(input("ingrese aqui el porcentaje, tiene que ser mayor a 1% : "))
                    if porcentajeManual >= 1:
                        valorConPropina = ((valorConPropina * (porcentajeManual/100) ) + valorConPropina)
                        return valorConPropina
                    else:
                        print("tiene que ser igual o mayor a 1%, intentalo denuevo..")
                except:
                    print("ingresa un porcentaje numerico..")
                    
def pagoIndividual_o_Divido():
    formadepago = int(input("""-----------------------------------------------------------------
quieres que el pago lo haga una sola persona o entre varias ?
1. pago individual
2. pago dividido
                        
        : """))
    if formadepago == 1:
        cantidadPersonas = 1
        print(f"pago por una sola persona {cantidadPersonas}")
        return cantidadPersonas
    elif formadepago == 2:
        cantidadPersonas = int(input("entre cuantas personas se va a realizar el pago? : "))
        print(f"pago por mas de una persona {cantidadPersonas} ")
        return cantidadPersonas
   
def pagoEquitativo_o_Desigual(personas, valorfactura):
    if personas > 1:
        formaDePago = int(input("""-------------------------------------------------------
el pago sera equitativo entre dichas personas:
1. pago equitativo
2. pago desigual (el pago desigual admite el pago maximo entre 3 personas.)

        : """))
        if formaDePago == 1:
            pago_por_persona = (valorfactura/personas)
            print(f"este es el pago por persona equitativamente {pago_por_persona}")
            codigoextendido = "pago equitativo"
            return pago_por_persona, codigoextendido
        elif formaDePago == 2:
            pago_por_persona = 0
            codigoextendido = int(input("""
dividir el pago desigualmente para:
1. 2 personas   
2. 3 personas
        : """))
            return pago_por_persona, codigoextendido
    else:       
        pago_por_persona = valorfactura
        codigoextendido = "pago individual"
        return pago_por_persona, codigoextendido
        
def pagoDesigual2personas(maximo3personas, valorfactura):    
    if maximo3personas == 1:
        verificadorPagoDesigual = "pago desigual2personas"
        valor100 = 100
        porcentajePersona1 = int(input("ingrese el porcentaje de l factura que pagara la persona 1: "))
        print(f"este es el porcentaje persona 1 {porcentajePersona1}")
        porcentajePersona2 = valor100 - porcentajePersona1
        print(f"este es el porcentaje persona 2 {porcentajePersona2}")
        pago_por_persona1 = (porcentajePersona1 / 100) * valorfactura
        print(f"este es el pago persona 1 {pago_por_persona1}")
        pago_por_persona2 = (porcentajePersona2 / 100) * valorfactura
        print(f"este es el pago persona 2 {pago_por_persona2}") 
        return verificadorPagoDesigual, pago_por_persona1, pago_por_persona2

    else:
        return
       
def pagoDesigual3personas(maximo3personas, valorfactura):
    if maximo3personas == 2:
        verificadorPagoDesigual = "pago desigual3personas"
        porcentajePersona1 = int(input("ingrese el porcentaje de l factura que pagara la persona 1: "))
        valor100 = 100 - porcentajePersona1
        print(f"este es el porcentaje persona 1 {porcentajePersona1}")
        porcentajePersona2 = int(input("ingrese el porcentaje de l factura que pagara la persona 2: "))
        valor100 = valor100 - porcentajePersona2
        print(f"este es el porcentaje persona 2 {porcentajePersona2}")
        porcentajePersona3 = valor100
        print(f"este es el porcentaje persona 3 {porcentajePersona3}")
        pago_por_persona1 = (porcentajePersona1 / 100) * valorfactura
        print(f"este es el pago persona 1 {pago_por_persona1}")
        pago_por_persona2 = (porcentajePersona2 / 100) * valorfactura
        print(f"este es el pago persona 2 {pago_por_persona2}")
        pago_por_persona3 = (porcentajePersona3 / 100) * valorfactura
        print(f"este es el pago persona 3 {pago_por_persona3}")
        return verificadorPagoDesigual , pago_por_persona1, pago_por_persona2, pago_por_persona3
                    
def main():
    print("------------------------CALCULADORA DE PROPINAS---------------------------")
    facturaOriginal = tomadelafacturaOriginal()
    divisa1 = escojerDivisa()
    facturaOriginal = eliminandoCaracteresInnecesarios(divisa1, facturaOriginal)
    valorApagar = calculandoPropina(facturaOriginal)
    cantidadDEpersonas = pagoIndividual_o_Divido()
    pagoporPersona, veriDesigual = pagoEquitativo_o_Desigual(cantidadDEpersonas, valorApagar)
    if veriDesigual == 2:
        veriDesigual, pago1, pago2, pago3 = pagoDesigual3personas(veriDesigual, valorApagar)    
        print(f"veriDesigual llego hasta aqui {veriDesigual}")
        print(f"pago por persona llego hasta aqui {pagoporPersona}")
        print(f"""
            la factura con un total de ${round(valorApagar, 2)}
            cancelada por {cantidadDEpersonas} persona(s)
            con un pago desigual es de {pago1} a pagar por la persona(1)
            con un pago desigual es de {pago2} a pagar por la persona(2)
            con un pago desigual es de {pago3} a pagar por la persona(3)
            """)        
    elif veriDesigual == "pago individual" or veriDesigual == "pago equitativo":
        print(f"""
            la factura con un total de ${round(valorApagar, 2)}
            cancelada por {cantidadDEpersonas} persona(s)
            es de {pagoporPersona} a pagar por persona(s)""")   
    elif veriDesigual == 1:
        veriDesigual, pago1, pago2 = pagoDesigual2personas(veriDesigual, valorApagar)
        print(f"""
            la factura con un total de ${round(valorApagar, 2)}
            cancelada por {cantidadDEpersonas} persona(s)
            con un pago desigual es de {pago1} a pagar por la persona(1)
            con un pago desigual es de {pago2} a pagar por la persona(2)
            """)

        
main()




















