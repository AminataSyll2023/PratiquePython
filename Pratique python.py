# Exerice1
def bissextile(annee):
    if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
        return True
    else:
        return False
annee = 2008
if bissextile(annee):
    print(f"L'année {annee} est bissextile.")
else:
    print(f"L'année {annee} n'est pas bissextile.")

annee = 2900
if bissextile(annee):
    print(f"L'année {annee} est bissextile.")
else:
    print(f"L'année {annee} n'est pas bissextile.")

annee = 2000
if bissextile(annee):
    print(f"L'année {annee} est bissextile.")
else:
    print(f"L'année {annee} n'est pas bissextile.")

# Exercice2
# QUESTION 2.1 :
import random
def lancer_deux_des():
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    somme = de1 + de2
    return somme
resultat = lancer_deux_des()
print("La somme de lancer de deux des est :",  resultat)

# QUESTION 2.2 :

def lancer_des(nombre_des):
    somme = 0
    i = 0
    for i in range(nombre_des):
        de = random.randint(1, 6)
        somme += de
    
    return somme 
resultat = lancer_des(2)
print("le résultat d’un lancer de deux dés est :", resultat )

resultat = lancer_des(3)
print( "le résultat d’un lancer de trois dés est :", resultat)

# Exercice3
def afficherSuiteCarres():
    n = int(input("Entrez un entier n : "))
    suite = [str(i**2) for i in range(n+1)]
    resultat = " - ".join(suite)
    print(" La suite des carrées jusqu’à", n , "est : ", resultat )
afficherSuiteCarres()

# Exercice4
def produit(n1, n2):
    # Vérification des valeurs de n1 et n2
    if n1 > n2:
        raise ValueError("n1 doit être inférieur ou égal à n2.")

    # Cas de base : si n1 et n2 sont égaux, le produit est égal à n1
    if n1 == n2:
        return n1

    # Appel récursif en réduisant l'intervalle de n1 à n2-1
    return n1 * produit(n1 + 1, n2)
resultat = produit(1, 5)
n1= int(input("Entrez un entier n1 : "))
n2 = int(input("Entrez un entier n2 : "))
calcule = produit(n1, n2)
print("Le produit des entiers aléatoires entre", n1, "et", n2, "est :", calcule)

#Exercice5
def nbPairImpair(tableau):
    nbr_pair = 0
    nbr_impair = 0
    for element in tableau:
        if element % 2 == 0:
            nbr_pair += 1
        else:
            nbr_impair += 1
    return nbr_pair, nbr_impair
tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
pair, impair = nbPairImpair(tableau)
print("Le nombre d'éléments pairs est :", pair)
print("Le nombre d'éléments impairs est :", impair)

# Exercice6
def decaleCircDroite(tableau):
    taille = len(tableau)
    tableau_decale = [0] * taille
    for i in range(taille):
        tableau_decale[(i + 1) % taille] = tableau[i]
    return tableau_decale
tableau = [12, 21, 10, 11, 0, 1, 6, 8]
print("Avant décalage circulaire à droite", tableau)
tableau_decale = decaleCircDroite(tableau)
print("Après décalage circulaire à droite", tableau_decale)

# Exercice7
# QUESTION 7.1 : DU BINAIRE VERS LE DÉCIMAL.
def bin2Dec(nBin):
    nDec = int(nBin, 2)
    return nDec
nBin = '10000001'
nDec = bin2Dec(nBin)
print('Le nombre binaire (code entier naturel) ' + str(nBin) + ' se convertit en base 10 : ' + str(nDec))

# QUESTION 7.2 : DU DÉCIMAL VERS LE BINAIRE.
def dec2Bin(nDec):
    if nDec == 0:
        return '0'
    else:
        bits = []
        while nDec > 0:
            bits.append(str(nDec % 2))
            nDec //= 2
        bits.reverse()
        return ''.join(bits)
nDec = 5 
nBin = dec2Bin(nDec)
print('Le nombre décimal ' + str(nDec) + ' s\'écrit en base 2 : ' + nBin)

# Exercice8
def sommeEntiers(n):
    if n == 1:
        return 1
    else:
        return n + sommeEntiers(n - 1)
n = int(input("Entrez la valeur de n : "))
somme = sommeEntiers(n)
print("La somme des", n, "premiers entiers est :", somme)

# Exercice9

def puissance(x, n):
    if n == 0:
        return 1
    else:
        return x * puissance(x, n - 1)
x = int(input("Entrez la valeur de x : "))
n = int(input("Entrez la valeur de n : "))
resultat = puissance(x, n)
print(x, "élevé à la puissance", n, "est égal à :", resultat)

# Exercice10
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Entrez la valeur de n : "))
resultat = fibonacci(n)
print("Le terme de la suite de Fibonacci à l'indice", n, "est :", resultat) 

# Exercice11
# Création du tableau contenant les chiffres de 1 à 10
tableau = list(range(1, 11))

# Conversion des chiffres en chaînes de caractères
tableau_str = list(map(str, tableau))

# Affichage des chiffres séparés par un point-virgule
resultat = "; ".join(tableau_str)
print(resultat)

# Exercice12
import random
def echanger(tableau, index1, index2):
    # Fonction pour échanger deux valeurs dans le tableau
    tableau[index1], tableau[index2] = tableau[index2], tableau[index1]

# Création du tableau contenant dix chiffres aléatoires entre 1 et 100
tableau = [random.randint(1, 100) for _ in range(10)]

# Affichage du tableau non trié
print("Tableau non trié :", tableau)

# Algorithme de tri à bulles
n = len(tableau)
for i in range(n-1):
    for j in range(n-1-i):
        if tableau[j] > tableau[j+1]:
            echanger(tableau, j, j+1)

# Affichage du tableau trié
tableau_str = list(map(str, tableau))
resultat = ", ".join(tableau_str)
print("Tableau trié :", resultat)

# Exercice13
def factorielle_recursive(n):
    if n == 0: 
        return 1
    else:
        return n * factorielle_recursive(n - 1)
n = int(input("Entrez un entier n : "))
factorielle = n * factorielle_recursive(n)
print("La factorielle de", n, "de manière récursive est :", factorielle)

# Exercice14
import random
def afficherPhraseAleatoire(tableau):
    phrase = ' '.join(random.sample(tableau, len(tableau)))
    print(phrase)
phrase = ["Je", "me", "nomme" , "Aminata", "Touré", "Syll"]
afficherPhraseAleatoire(phrase)