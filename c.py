import d

d.Creare_Graf(d.matrice_adiacenta, d.numar_noduri)
ok = 1
while int(ok) > 0 and int(ok) < 5 :
    print("1.Afisare graf")
    print("2.Determinarea daca graful este conex")
    print("3.Determinarea componentelor conexe ale grafului")
    print("4.Determinarea daca graful are cicluri")
    print("0.Inchidere program")
    print("Optiunea dumneavoastra :")
    ok = input()
    if int(ok) == 1 :
        d.Afisare_Graf(d.matrice_adiacenta, d.numar_noduri)
    if int(ok) == 2 :
       d.Graf_Conex(d.matrice_adiacenta, d.numar_noduri)
    if int(ok) == 3 :
        d.Componente_Conexe(d.matrice_adiacenta, d.numar_noduri)
    if int(ok) == 4 :
        if d.Cicluri(d.matrice_adiacenta, d.numar_noduri) == 1 :
            print("Graful are cicluri")
        else :
            print("Graful nu are cicluri")
    if int(ok) == 0 :
        k = 5















