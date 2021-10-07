
print ("Bienvenido \n\nEste es un sencillo programa para verificar que un numero especifico o rango de numeros cumplan las condiciones de la conjetura de Collatz, que dice que sea cual sea el número x inicial, tras un número finito de repeticiones de la operación se llega a 1.")
print ("(Solo son validos valores naturales mayores a 0)\n")


op = int(input("Si desea confirmar un numero especifico digite 1 \nsi desea confirmar un rango de numeros digite 2\n: "))
if op == 1:
    exit == 0
    while exit != 0:
        x = int(input("Dijite el numero que desea verificar: "))
        print (x)
        nom = x
        while x > 1:
            if x % 2 == 0:
                x= x/2
            else:
                x= (3*x)+1
            print (x)
        if x == 1:
            print ("\nLa conjetura de Collatz se cumple para: ", nom,"\n")
        else:
           print ("\nLa conjetura de Collatz no se cumplio con ", nom ," !!, Que raro! \n")
        exit = int(input("\nSi desea continuar, dijite 1. De lo contrario dijite 0\n"))
else:
    exit == 0
    while exit != 0:
        print ("Digite el primer y ultimo numero del rango respectivamente:")
        i = int(input("Numero inicial: "))
        f = int(input("Numero final: "))
        f=f+1
        for x in range(i,f):
            evento = 0
            nom = x
            while x > 1:
                if x % 2 == 0:
                    x= x/2
                else:
                    x= (3*x)+1
            print(nom ,"termino en ", x)
            if x != 1:
                evento =+ 1
                print ("\nHa ocurrido un evento inesperado!!\n")
        if evento != 0:
            print("\nSe descubrio (", evento ,") evento inesperado")
        else: 
            print ("\nLa conjetura de Collatz se cumplio para todos los numeros del rango")
        exit = int(input("\nSi desea continuar, dijite 1. De lo contrario dijite 0\n"))

