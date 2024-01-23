#--------------------------------CALCULADORA DE PROPINAS------------------------------
# version 1.0
# en esta version estan las funciones base del programa tanto las matematicas como 
# la inicial donde quise probar la libreria re y por medio de esta eliminar los
# los caracteres strings del input principal.
# dejando las funcionalidades que le quiero añadir abajo como comentarios.
import re
#   PENDIENTE:
    #ESCOJER DIVISA USD O COP
    #ESCOJER PORCENTAJE DE PROPINA MANUALMENTE
    #ESCOJER SI SE QUIERE PAGAR LA FACTURA DE FORMA INDIVIDUAL O ENTRE CUANTAS PERSONAS
    #SI ES ENTRE VARIAS PERSONAS SERA DE FORMA EQUITATIVA O DESIGUAL?
    #MANEJO DE EXEPCIONES PARA CADA MENU
    #LIMPIEZA DE CODIGO

def tomadelafacturaOriginal():
    factura1 = input("porfavor ingrese la factura total de hoy: ")
    print(factura1)
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
        print(factura1)
        factura1 = tomadelafacturaOriginal()
        return factura1

def eliminandoCaracteresInnecesarios(valorList):
    pattern =r"\w[a-zA-Z]+\s+"
    new_text = re.sub(pattern, "", valorList)     
    print("Texto modificado:", new_text)
    valorList = list(new_text)
    print(valorList)
    analphabeticList = ["m","y","."," ","",",","-", ":", ";", "!", "?", "'", "\""] 
    for character in analphabeticList: 
        if character in valorList: 
            valorList.remove(character) 
            print(valorList)
    valueCharacters = ["$"]   
    for character1 in valueCharacters: 
        if character1 in valorList: 
            valorList.remove(character1) 
            print(valorList)
    return valorList       
  
def calculandoPropina(valorConPropina):
    print(valorConPropina)
    while True:
        porcentaje_propina = input("""----------------------------------------------------
ahora escoje el porcentaje de propina que quieres aplicar
a la factura:
1. para el 18%
2. para el 20%
3. para el 25%
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
        
def main():
    print("------------------------CALCULADORA DE PROPINAS---------------------------")
    facturaOriginal = tomadelafacturaOriginal()
    facturaOriginal = eliminandoCaracteresInnecesarios(facturaOriginal)
    valorApagar = calculandoPropina(facturaOriginal)
    print(f" el valor que tienes a pagar son : ${valorApagar}")
    
main()




















