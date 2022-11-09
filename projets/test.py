#ECRIRE "bonsoir paris"
# r=12000
# s=1250
# e=10
# rh=230
# assertionUn = (((365*3)/(24-(16-8)))*(rh)>r)==(e*s<r) #false
# assOne = (15740,625 > 12000) #true
# asstwo = (12500<12000) #false
# assertionUn = (15740,625 > 12000)==(12500<12000) #false    
# #assertion2 = (((365*3)/(4-(12-8)))*(rh)>r)==(e*s<r) #true
# assOne = (1095/0>12000) #False
# asstwo = (12500<12000) #false                                       


# def retournerSixPlusTrois():
#     return 6+3
# def retournerSixPlusX(x):
#     return 6 + x
# #print("Qui vole un" + retournerSixPlusTrois() + "vole un boeuf")
# print(retournerSixPlusX(3))

# def add(x;y):
#     return x+y
# def sub(x;y):
#     return x-y
# def divide(x;y):
#     return x/y
# def multiply(x;y):
#     return x*y
# def modulo(x;y):
#     return x%y
# 19.58jour ouvrée par mois
# 8h ouvrée par jour

# def calculeSalaireSeconde(Salaire,j,h,s):
#     return Salaire/(j*h*s)

# print(calculeSalaireSeconde(1200,19.58,8,3600))

# def calculeSalaireHeure(Salaire,j,h):
# #     return Salaire/(j*h) 

# # print(calculeSalaireHeure(1200,19.58,8))
        
# # def calculeSalaireBrutEnNet(salaireBrut, coeff):
# #     # Calcul du coefficient pour 24% de taxe sur les salaires
# #     coeff= 1-(24/100)
# #     # Calcul du salaire net
# #     return salaireBrut * coeff

# def withdrawFees(total, percent):
#     # Calcul du montant des taxes a retirer
#     fees = total * (percent / 100)
#     #retourner la valeur totale moins les taxes
#     return total - fees

# def calculeSalaireNet(salaireBrut, coeff):
#     # Calculer et reourner le salaire Net a partir du salire brut
#     return withdrawFees(salaireBrut, coeff)

# def divide(x,y):
#     # si Y est égal a 0 alors la division est impossible
#     if y==0:
#     # alors renvoyer un message d'erreur
#         print("Bah alors ?")
#         return None
#     #Sinon
#     else:
#     #retourner le calcul x/y
#         return x/y

# def input():
    # renvoie un carctère de type string au hasard
     


# def miniJeux(char):
#     char = input()
#     # récupérer une lettre aléatoire et l'affecter a une variable
#     #tant que le charactère n'est pas 'a' 
#     while char != "a":
#         # regénère un charactère aléatoire
#         char = input()
#         # si le charactère regénéré n'est pas 'a' alors la boucle continue
#     print("gg")
#     return
#     # Affiche gg

# tableau = [1,5,9,5,7,32,89]

# #pour récupéré 7 je prends dans le tableau l'index 4
# print(tableau[4])

# len(tableau)
# print(len(tableau))

# prénom = "Dydy"
# nom = "ben"
# id = nom + ' ' + prénom

# integerValue = 10
# stringIntegerValue = str(10)

#exo 1 
# concatene 2 chaine de charactère, les séparant par une virgule

# fonction affichant l'identité d'une personne
def chaineResultat(strA, strB):
     # assigner a stringfiedStrA le retour de l'execution de la fonction str with comme paramètre strA
     stringifiedStrA= str(strA)
     # assigner a stringfiedStrA le retour de l'execution de la fonction str with comme paramètre strB
     stringifiedStrB= str(strB)
     # calcule de l'id concatenat les 2 chaine de carctère et en les séparant par une virgule
     chaineResultat = stringifiedStrA + ', ' + stringifiedStrB
     # retourner chaineResultat
     return chaineResultat
print(chaineResultat(strA="j'aime la moula" , strB="la grosse moula sa mère"))

#exo2
# Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractère
#avec l'ensemble des occurence d'un chiffre
#pour tableau [0,1,1,1,0,1,1,0,1]
#la fonction(tableau, 0) doit renvoyer "0, 4, 7" n'hesitez pas a implementer la première fonction ;)

# définir la fonction findIndexes avec comme paramètres une liste tableau et x quelconque
# def findIndexes(tableau , x):
#     # initialisation de la variable i a 0
#     i = 0
#     # initialisation de la variable chaineRetour a chaine de charactère vide
#     chaineRetour = ""
#     # tant que i est plus petit que le nombre d'élément dans le tableau 
#     while i < len(tableau):
#         # alors on assigne a selected la valeur présente a la position i du tableau
#         selected = tableau[i]
#         # on initialise isFirst a vrai
#         isFirst = True
#         # si selected est égal a x
#         if selected == x:
#             # alors 
#             #Si isfirst est vrai
#             if isFirst:
#                 # Alors on assigne a chaineRetour la waleur de i
#                 chaineRetour = i
#                 # changer is first en faux
#                 isFirst = False
#         # sinon     
#         else:       
#             # assigner le retour de l'execution de la fonction chaineResultat avec comme paramètre chaineRetour et i
#             chaineRetour = chaineResultat(chaineRetour, i)
#         # assigner a i, i auquel on ajoute 1
#         i = i + 1
#     # retourner chaineRetour
#     return chaineRetour

#definir une fonction suiteDeFibonacci avec comme paramètre x et lenmax

#FIN   