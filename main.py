op = int(input("Si desea confirmar un numero especifico digite 1 \nsi desea confirmar un rango de numeros digite 2\n: "))
if op == 1:
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
else:
    print ("Digite el primer y ultimo numero del rango respectivamente:")
    i = int(input("Numero inicial: "))
    f = int(input("Numero final: "))
    for x in range(i,f):
        nom = x
        while x > 1:
            if x % 2 == 0:
                x= x/2
            else:
                x= (3*x)+1
        print(nom ,"termino en ", x)
        
