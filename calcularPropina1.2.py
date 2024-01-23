#--------------------------------CALCULADORA DE PROPINAS------------------------------
# version 1.2
# En esta version se corrijieron todas los posibles saltos de exepciones que nos detendrian el programa
# ademas de prints innecesarios que solo me mostraban como se iban transformando las variables
# soy consiente de que se puede mejorar mucho, un ejemplo en la funcion main() todos los prints
# finales se podrian introducir de la funcion de donde provienen los valores y asi dejar una funcion 
# main mucho mas limpia y estetica.. cosa que dejare para otra ocasion, para asi seguir con otros proyectos.

import re
    #PENDIENTE:
    # OPTIMIZAR AL GUSTO...

def tomadelafacturaOriginal():
    factura1 = input("porfavor ingrese la factura total de hoy: ")
    while True:
        try:
            verificador = int(input(f"""---------------------------------------------------------------------
estas seguro que este fue el valor de la factura?: 
1. confirmar
2. rechazar
-------------------------------------------------------------------------
            : """))
            if verificador == 1:
                return factura1
            elif verificador == 2:
                factura1 = tomadelafacturaOriginal()    
        except:
            print("----------Ingresa ""1"" para ACEPTAR o ""2"" para RECHAZAR----------")
            print("--------------------------------------------------------------------")

def escojerDivisa():
    while True:
        try:
            divisaEscojida = int(input("""que divisa estas manejando en esta factura?: 
1. USD (dolares estadounidenses)
2. COP (pesos colombianos)
                           """))
            if divisaEscojida == 2:
                return divisaEscojida
            elif divisaEscojida == 1:
                return divisaEscojida
        except:
            print("------------Ingresa ""1"" para USD o ""2"" para COP-----------------")
            print("--------------------------------------------------------------------")
            
def eliminandoCaracteresInnecesarios(divisa, valorList):
    pattern =r"\w[a-zA-Z]+\s+"
    new_text = re.sub(pattern, "", valorList)     
    valorList = list(new_text)
    if divisa == 2:
        analphabeticList1 = ["m","y","."," ","","$",",","-",":", ";", "!", "?", "'", "\""] 
        for character in analphabeticList1: 
            while character in valorList: 
                valorList.remove(character)
        return valorList
    elif divisa == 1:
        analphabeticList = ["m","y"," ","","$",",","-", ":", ";", "!", "?", "'", "\""]
        for character in analphabeticList: 
            if character in valorList: 
                valorList.remove(character) 
        return valorList
            
def calculandoPropina(valorConPropina):
    valorConPropina = float(''.join(valorConPropina))
    while True:
        try:
            porcentaje_propina = int(input("""----------------------------------------------------
ahora escoje el porcentaje de propina que quieres aplicar
a la factura:
1. para el 18%
2. para el 20%
3. para el 25%
4. Para ingresar un porcentaje manualmente
            : """))
            
            if porcentaje_propina == 1:
                valorConPropina = ((valorConPropina * 0.18) + valorConPropina)
                return valorConPropina
            elif porcentaje_propina == 2:
                valorConPropina = ((valorConPropina * 0.20) + valorConPropina)
                return valorConPropina
            elif porcentaje_propina == 3:
                valorConPropina = ((valorConPropina * 0.25) + valorConPropina)
                return valorConPropina
            elif porcentaje_propina == 4:
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
            else:
                print("ingresa un numero entre 1 y 4 en el menu numerico para escojer tu porcentaje de propina")
                print("---------------------------------------------------------------------------------------")
        except:
            print("ingresa un numero entre 1 y 4 en el menu numerico para escojer tu porcentaje de propina")
            print("---------------------------------------------------------------------------------------")         
                    
def pagoIndividual_o_Divido():
    while True:
        try:
            formadepago = int(input("""-----------------------------------------------------------------
quieres que el pago lo haga una sola persona o entre varias ?
1. pago individual
2. pago dividido
                        
        : """))
            if formadepago == 1:
                cantidadPersonas = 1 
                return cantidadPersonas
            elif formadepago == 2:
                cantidadPersonas = int(input("entre cuantas personas se va a realizar el pago? : "))
                return cantidadPersonas
        except:
            print("----Ingresa ""1"" para pago individual o ""2"" para pago dividido---")
            print("--------------------------------------------------------------------")
               
def pagoEquitativo_o_Desigual(personas, valorfactura):
    while True:
        try:    
            if personas > 1:
                formaDePago = int(input("""-------------------------------------------------------
el pago sera equitativo entre dichas personas:
1. pago equitativo
2. pago desigual (el pago desigual admite el pago maximo entre 3 personas.)

        : """))
                if formaDePago == 1:
                    pago_por_persona = (valorfactura/personas)
                    codigoextendido = "pago equitativo"
                    return pago_por_persona, codigoextendido
                elif formaDePago == 2:
                    pago_por_persona = 0
                    while True:
                        try:
                            codigoextendido = int(input("""
dividir el pago desigualmente para:
1. 2 personas   
2. 3 personas
        : """))
                            if codigoextendido == 1:
                                return pago_por_persona, codigoextendido
                            elif codigoextendido == 2:
                                return pago_por_persona, codigoextendido
                            else:
                                print("el numero debe ser entre 1 y 2 ")                      
                        except:
                            print("---------Ingresa ""1"" para 2 personas o ""2"" para 3 personas------")
                            print("--------------------------------------------------------------------")
            else:       
                pago_por_persona = valorfactura
                codigoextendido = "pago individual"
                return pago_por_persona, codigoextendido
            
        except:
            print("----ingresa ""1"" para pago equitativo o ""2"" para pago desigual---")
            print("--------------------------------------------------------------------")
        
def pagoDesigual2personas(personas2, valorfactura):
    if personas2 == 1:
        verificadorPagoDesigual = "pago desigual2personas"
        valor100 = 100
        while True:
            try:
                porcentajePersona1 = int(input("ingrese el porcentaje de la factura que pagara la persona 1: "))
                if porcentajePersona1 < valor100:
                    print(f"este es el porcentaje persona 1 {porcentajePersona1}%")
                    porcentajePersona2 = valor100 - porcentajePersona1
                    print(f"este es el porcentaje persona 2 {porcentajePersona2}%")
                    pago_por_persona1 = (porcentajePersona1 / 100) * valorfactura
                    pago_por_persona2 = (porcentajePersona2 / 100) * valorfactura 
                    return verificadorPagoDesigual, pago_por_persona1, pago_por_persona2
                else:
                    print("el porcentaje ingresado tiene que ser menor a 100%")
            except:
                print("--------recuerda ingresar el porcentaje que pagara la persona 1-----")
                print("--------------------------------------------------------------------")
       
def pagoDesigual3personas(personas3, valorfactura):
    if personas3 == 2:
        verificadorPagoDesigual = "pago desigual3personas"
        valor100 = 100
        while True:
            try:    
                porcentajePersona1 = int(input("ingrese el porcentaje de la factura que pagara la persona 1: "))
                if porcentajePersona1 < valor100:
                    valor100 = 100 - porcentajePersona1
                    print(f"este es el porcentaje persona 1 {porcentajePersona1}%")
                    porcentajePersona2 = int(input("ingrese el porcentaje de la factura que pagara la persona 2: "))
                    if porcentajePersona2 <= porcentajePersona1 and porcentajePersona2 <= valor100:
                        valor100 = valor100 - porcentajePersona2
                        print(f"este es el porcentaje persona 2 {porcentajePersona2}%")
                        porcentajePersona3 = valor100
                        print(f"este es el porcentaje persona 3 {porcentajePersona3}%")
                        pago_por_persona1 = (porcentajePersona1 / 100) * valorfactura
                        pago_por_persona2 = (porcentajePersona2 / 100) * valorfactura
                        pago_por_persona3 = (porcentajePersona3 / 100) * valorfactura
                        return verificadorPagoDesigual , pago_por_persona1, pago_por_persona2, pago_por_persona3
                    else:
                        print("recuerda que el porcentaje de la persona 1 y 2 juntos no pueden exceder mas del 100""%"" de la factura")
                else:
                    print("el porcentaje tiene que ser menor que 100%")
            except:
                print("-----------------ingresa un valor numerico...-----------------------")
                print("--------------------------------------------------------------------")
                    
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
        print(f"""
            la factura con un total de ${round(valorApagar, 2)}
            cancelada por 3 persona(s)
            con un pago desigual es de {round(pago1, 2)} a pagar por la persona(1)
            con un pago desigual es de {round(pago2, 2)} a pagar por la persona(2)
            con un pago desigual es de {round(pago3, 2)} a pagar por la persona(3)
            """)        
    elif veriDesigual == "pago individual" or veriDesigual == "pago equitativo":
        print(f"""
            la factura con un total de ${round(valorApagar, 2)}
            cancelada por {cantidadDEpersonas} persona(s)
            es de {round(pagoporPersona, 2)} a pagar por persona(s)""")   
    elif veriDesigual == 1:
        veriDesigual, pago1, pago2 = pagoDesigual2personas(veriDesigual, valorApagar)
        print(f"""
            la factura con un total de ${round(valorApagar, 2)}
            cancelada por 2 persona(s)
            con un pago desigual es de {round(pago1, 2)} a pagar por la persona(1)
            con un pago desigual es de {round(pago2, 2)} a pagar por la persona(2)
            """)

        
main()




















