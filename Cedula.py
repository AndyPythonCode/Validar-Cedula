"""
Explicacion
https://www.youtube.com/watch?v=__Ko7VxoCuU&feature=youtu.be
Ayudo bastante esa explicacion
"""

def validarCedula(valor):
    limpiar = valor.replace('-','') # limpiamos el valor que nos pasa si tiene -
    cedula = limpiar[0:len(limpiar)-1] # almacenamos valos limpio sin identificador
    verificador = limpiar[len(limpiar)-1:] # sacamos el verificador el ultimo valor
    resultado = 0 # Suma de todos
    INTERCALAR = [1,2,1,2,1,2,1,2,1,2] # constante que se necesita
    #print(f"limpiamos:{limpiar} | cedula: {cedula} | verificador: {verificador}")
    if len(limpiar) == 11: # Verificamos si tiene 11 digitos lo estandar
        if limpiar.isdigit(): # Si son valores numeros
            for i in range(len(cedula)): # recoremos la longitud de cedula sin verificador
                x = int(cedula[i])*INTERCALAR[i] # multiplicamos por constante
                if x >= 10:# si el valor es mayor o igual a 10 se suman separados
                    separar = list(str(x)) # separamos el valor 1 y 2 si son mayores
                    x = int(separar[0]) + int(separar[1]) # sumamos y guardamos en ella misma
                resultado += x # siempre guadamos en resutaldo para ir amacenando valor
            cambiarUltimo = int(list(str(resultado))[0]+"0")# cambiamos el ultimo numero por 0
            decenaSuperior = cambiarUltimo+10 # sumamos 10 para asi poder llegar a la decenaSuperior mas cercana
            if(decenaSuperior-resultado) == int(verificador) or (resultado-cambiarUltimo) == int(verificador):
                return "\nCedula Validad :D"#Dos opiciones: que la decenaSuperior sea igual que resultado o no.
            else:
                return "\nCedula Invalidad :( !!"# Si no comple ninguna no es valida
        else:
            return "\nNo son numeros!!"# Si encuentra una letra tampoco
    else:
        return "\nValor de digitos estandar fuera de rango!!"# si es valor o menor a 11 no comple estandar

def capturarValor(Pregunta):
    mensaje = input(Pregunta)
    return mensaje