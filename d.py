print("Introduceti numarul de noduri :")
numar_noduri = input()
print("Introduceti numarul de muchii :")
muchii = input()
numar_maxim_muchii = (int(numar_noduri) * (int(numar_noduri) - 1)) / 2
while int(muchii) > int(numar_maxim_muchii) :
    print("Introduceti alt numar(prea mare) :")
    muchii = input()
matrice_adiacenta = [[0 for i in range(int(numar_noduri))] for j in range(int(numar_noduri))]

def Creare_Graf(matrice, n) :
    k = 0
    print("Introduceti muchiile :")
    while int(k) < int(muchii) :
        i = input("nodul de plecare = ")
        j = input("nodul de sosire = ")
        if int(i) == int(j) :
            print("Nodul de plecare nu poate fi identic cu nodul de iesire. Introduceti alte noduri :")
            i = input("nodul de plecare = ")
            j = input("nodul de sosire = ")
        matrice_adiacenta[int(i) - 1][int(j) - 1] = 1
        matrice_adiacenta[int(j) - 1][int(i) - 1] = 1
        k += 1

def Afisare_Graf(matrice, n) :
    i = 0
    while int(i) < int(numar_noduri) :
        print(matrice[i][0:])
        i += 1

viz = []
i = 0
while int(i) < int(numar_noduri) :
    viz.append(0)
    i += 1

def DFS(nod,matrice,n) :
    i = 0
    viz[nod] = 1
    while int(i) < int(numar_noduri) :
        if matrice_adiacenta[nod][i] == 1 and viz[i] == 0 :
            DFS(i,matrice,n)
        i += 1
    return viz

def Graf_Conex(matrice, n) :
    DFS(0, matrice, n)
    i = 0
    ok = 1
    while int(i) < int(numar_noduri) :
        if viz[i] == 0 :
            ok = 0
        i += 1
    if ok == 1 :
        print("Graful este conex")
    else :
        print("Graful nu este conex")

def Componente_Conexe(matrice, n) :
    DFS(0, matrice, n)
    i = 0
    print("Componenta conexa :")
    while int(i) < int(numar_noduri) :
        if viz[i] == 1 :
            print(i + 1)
        else :
            DFS(i, matrice, n)
            i -= 1
            print("Componenta conexa este: ")
        i += 1

def Grad_Nod(nod, matrice, n) :
    i = 0
    nr = 0
    while int(i) < int(n) :
        if matrice[nod][i] == 1 :
            nr += 1
        i += 1
    return nr
            
def Cicluri(matrice , n) :
    i = 0
    while int(i) < int(n) :
        if Grad_Nod(i, matrice , n) > 1 :
            DFS(i, matrice, n)
            nr = 0
            j = 0
            while int(j) < int(n) :
                if matrice[i][j] == 1 and viz[j] == 1 :
                    nr += 1
                j += 1
            if int(nr > 1) :
                return 1
        i += 1
    return 0
