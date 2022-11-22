#importe input qui prend les entrés des joueur
#deffinir la fonction StartGame
# import pygame
# pygame.init()
# from pygame.locals import *
# fenetre = pygame.display.set_mode((1000, 1000))
# pygame.display.set_caption("Morpion")

# interface = True
# while interface:
#     pygame.rect(255.255)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             interface = False
    

# pygame.quit()


# assigner la variable coordonne la liste ['',"A","B","C"]
coordonne = ['',"A","B","C"]
# assigner a la variable ligneUn la liste ["1","","",""]
ligneUn =["1","","",""]
# assigner a la variable ligneDeux la liste ["2","","",""]
ligneDeux =["2","","",""]
# assigner a la variable ligneTrois la liste ["3","","",""]
ligneTrois =["3","","",""]
# initialiser la variable compteTour a 0
compteTour = 0
# initialiser la variable encore a 0
encore = 0

# assigner a la variable colonneUn la liste [ligneUn[1],ligneDeux[1],ligneTrois[1]]
colonneUn = [ligneUn[1],ligneDeux[1],ligneTrois[1]]
# assigner a la variable colonneDeux la liste [ligneUn[2],ligneDeux[2],ligneTrois[2]]
colonneDeux = [ligneUn[2],ligneDeux[2],ligneTrois[2]]
# assigner a la variable colonneDeux la liste [ligneUn[3],ligneDeux[3],ligneTrois[3]]
colonneTrois = [ligneUn[3],ligneDeux[3],ligneTrois[3]]
# assigner a la variable diagoUn la liste [colonneUn[0],colonneDeux[1],colonneTrois[2]]
diagoUn = [colonneUn[0],colonneDeux[1],colonneTrois[2]]
# assigner a la variable diagoDeux la liste [colonneUn[2],colonneDeux[1],colonneTrois[0]]
diagoDeux = [colonneUn[2],colonneDeux[1],colonneTrois[0]]

# initialiser la variable Jun a 0
Jun = 0
# initialiser la variable Jdeux a 0
Jdeux = 0
# initialiser la variable gagnant a 3
gagnant = 3
# assigner a la variable Tableau la liste [coordonne,ligneUn,ligneDeux,ligneTrois]
Tableau = [coordonne,ligneUn,ligneDeux,ligneTrois]

# definition de la fonction Restart
def Restart():
    # globaliser la variable ligneDeux
    global ligneDeux
    # globaliser la variable ligneUn
    global ligneUn
    # globaliser la variable ligneTrois
    global ligneTrois
    # globaliser la variable colonneDeux
    global colonneDeux
    # globaliser la variable colonneUn
    global colonneUn
    # globaliser la variable colonneTrois
    global colonneTrois
    # globaliser la variable diagoDeux
    global diagoDeux
    # globaliser la variable diagoUn
    global diagoUn
    # globaliser la variable gagnant
    global gagnant
    # globaliser la variable Jun
    global Jun
    # globaliser la variable Jdeux
    global Jdeux
    # globaliser la variable compteTour
    global compteTour
    # globaliser la variable encore
    global encore
    # globaliser la variableT Tableau
    global Tableau
    # affiche "yo bande de débile tu veux retenter ?"
    print("yo bande de débile tu veux retenter ?")
    # assigne a la variable encore le retour d'éxecutien de la fonction input de paramètre "-1 = retenter || -2 = j'abandone car jsui nul: "
    encore = input("-1 = retenter || -2 = j'abandone car jsui nul: ")
    # si la variable encore n'est pas dans la liste ['1','2']
    if not encore in ['1','2']:
        # alors afficher "te fous pas dma geu ptit batard mes 1 ou 2 et pas : ",encore
        print("te fous pas dma geu ptit batard mes 1 ou 2 et pas : ",encore)
        # afficher "yo bande de débile vous voulez retenter ?"
        print("yo bande de débile vous voulez retenter ?")
        # éxécute la fonction Restart
        Restart()
    # si la variable encore est dans la liste ['1','2']
    elif encore in ['1','2']:
        # alors si la variable encore est = a 1
        if encore == '1':
            # alors afficher "oki Dinosaure ON RESTARTTTTTTTRE"
            print("oki Dinosaure ON RESTARTTTTTTTRE")
            # assigne a la variable coordone la liste ['',"A","B","C"]
            coordonne = ['',"A","B","C"]
            # assigne a la variable ligneUn la liste ["1","","",""]
            ligneUn =["1","","",""]
            # assigne a la variable ligneDeux la liste ["2","","",""]
            ligneDeux =["2","","",""]
            # assigne a la variable ligneTrois la liste ["3","","",""]
            ligneTrois =["3","","",""]
            # réinitializer a la variable compteTour a 0
            compteTour = 0
            # réinitializer a la variable encore a 0
            encore = 0
            # assigne a la variable colonneUn la liste [ligneUn[1],ligneDeux[1],ligneTrois[1]]
            colonneUn = [ligneUn[1],ligneDeux[1],ligneTrois[1]]
             # assigne a la variable colonneDeux la liste [ligneUn[2],ligneDeux[2],ligneTrois[2]]
            colonneDeux = [ligneUn[2],ligneDeux[2],ligneTrois[2]]
             # assigne a la variable colonneTrois la liste [ligneUn[3],ligneDeux[3],ligneTrois[3]]
            colonneTrois = [ligneUn[3],ligneDeux[3],ligneTrois[3]]
             # assigne a la variable diagoUn la liste [colonneUn[0],colonneDeux[1],colonneTrois[2]]
            diagoUn = [colonneUn[0],colonneDeux[1],colonneTrois[2]]
             # assigne a la variable diagoDeux la liste [colonneUn[2],colonneDeux[1],colonneTrois[0]]
            diagoDeux = [colonneUn[2],colonneDeux[1],colonneTrois[0]]
            # réinitialize la variable Jun a 0
            Jun = 0
            # réinitialize la variable Jdeux a 0
            Jdeux = 0
            # réinitialize la variable gagnant a 3
            gagnant = 3
            # assigne a la variable Tableau la liste [coordonne,ligneUn,ligneDeux,ligneTrois]
            Tableau = [coordonne,ligneUn,ligneDeux,ligneTrois]
            # éxecute la fonction StarterGame
            StarterGame()
        # si la variable encore = a 2
        elif encore == '2':
            # alors afficher "NNNNNNNNNNNNNNOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBBBBBBBBBBBBBB"
            print("NNNNNNNNNNNNNNOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBBBBBBBBBBBBBB")
            # retourne la fonction
            return
# definir la fonction winner
def winner():
    # globaliser la variable ligneDeux
    global ligneDeux
    # globaliser la variable ligneUn
    global ligneUn
    # globaliser la variable ligneTrois
    global ligneTrois
    # globaliser la variable colonneDeux
    global colonneDeux
    # globaliser la variable colonneUn
    global colonneUn
    # globaliser la variable colonneTrois
    global colonneTrois
    # globaliser la variable diagoDeux
    global diagoDeux
    # globaliser la variable diagoUn
    global diagoUn
    # globaliser la variable gagnant
    global gagnant
    # assigne a la variable colonneUn la liste [ligneUn[1],ligneDeux[1],ligneTrois[1]]
    colonneUn = [ligneUn[1],ligneDeux[1],ligneTrois[1]]
    # assigne a la variable colonneDeux la liste [ligneUn[2],ligneDeux[2],ligneTrois[2]]
    colonneDeux = [ligneUn[2],ligneDeux[2],ligneTrois[2]]
    # assigne a la variable colonneTrois la liste [ligneUn[3],ligneDeux[3],ligneTrois[3]]
    colonneTrois = [ligneUn[3],ligneDeux[3],ligneTrois[3]]
    # assigne a la variable diagoUn la liste [colonneUn[0],colonneDeux[1],colonneTrois[2]]
    diagoUn = [colonneUn[0],colonneDeux[1],colonneTrois[2]]
    # assigne a la variable diagoDeux la liste [colonneUn[2],colonneDeux[1],colonneTrois[0]]
    diagoDeux = [colonneUn[2],colonneDeux[1],colonneTrois[0]]
    # si la variable ligneUn[1], ligneUn[2], ligneUn[3] est égal a x
    if ligneUn[1] == "x" and ligneUn[2] == "x" and ligneUn[3] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable ligneDeux[1], ligneDeux[2], ligneDeux[3] est égal a x
    elif ligneDeux[1] == "x" and ligneDeux[2] == "x" and ligneDeux[3] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable ligneTrois[1], ligneTrois[2], ligneTrois[3] est égal a x
    elif ligneTrois[1] == "x" and ligneTrois[2] == "x" and ligneTrois[3] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable colonneUn[0], colonneUn[1], colonneUn[2] est égal a x
    elif colonneUn[0] == "x" and colonneUn[1] == "x" and colonneUn[2] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable colonneDeux[0], colonneDeux[1], colonneDeux[2] est égal a x
    elif colonneDeux[0] == "x" and colonneDeux[1] == "x" and colonneDeux[2] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable colonneTrois[0], colonneTrois[1], colonneTrois[2] est égal a x
    elif colonneTrois[0] == "x" and colonneTrois[1] == "x" and colonneTrois[2] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable diagoUn[0], diagoUn[1], diagoUn[2] est égal a x
    elif diagoUn[0] == "x" and diagoUn[1] == "x" and diagoUn[2] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable diagoDeux[0], diagoDeux[1], diagoDeux[2] est égal a x
    elif diagoDeux[0] == "x" and diagoDeux[1] == "x" and diagoDeux[2] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable ligneUn[1], ligneUn[2], ligneUn[3] est égal a o
    elif ligneUn[1] == "o" and ligneUn[2] == "o" and ligneUn[3] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable ligneDeux[1], ligneDeux[2], ligneDeux[3] est égal a o
    elif ligneDeux[1] == "o" and ligneDeux[2] == "o" and ligneDeux[3] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable ligneTrois[1], ligneTrois[2], ligneTrois[3] est égal a o
    elif ligneTrois[1] == "o" and ligneTrois[2] == "o" and ligneTrois[3] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable colonneUn[0], colonneUn[1], colonneUn[2] est égal a o
    elif colonneUn[0] == "o" and colonneUn[1] == "o" and colonneUn[2] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable colonneDeux[0], colonneDeux[1], colonneDeux[2] est égal a o
    elif colonneDeux[0] == "o" and colonneDeux[1] == "o" and colonneDeux[2] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable colonneTrois[0], colonneTrois[1], colonneTrois[2] est égal a o
    elif colonneTrois[0] == "o" and colonneTrois[1] == "o" and colonneTrois[2] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable diagoUn[0], diagoUn[1], diagoUn[2] est égal a o
    elif diagoUn[0] == "o" and diagoUn[1] == "o" and diagoUn[2] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable diagoDeux[0], diagoDeux[1], diagoDeux[2] est égal a o
    elif diagoDeux[0] == "o" and diagoDeux[1] == "o" and diagoDeux[2] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si compteTour est égal a 9
    elif compteTour == 9:
        # alors assigne a la variable gagnant, 0
        gagnant = 0
# definir la fonction coupJoueur
def coupJoueur():
    # globaliser la variable ligneDeux
    global ligneDeux
    # globaliser la variable ligneUn
    global ligneUn
    # globaliser la variable ligneTrois
    global ligneTrois
    # globaliser la variable colonneDeux
    global colonneDeux
    # globaliser la variable colonneUn
    global colonneUn
    # globaliser la variable colonneTrois
    global colonneTrois
    # globaliser la variable diagoDeux
    global diagoDeux
    # globaliser la variable diagoUn
    global diagoUn
    # globaliser la variable gagnant
    global gagnant
    # assigner a la variable reponse, le retour de l'éxecution de la fonction input avec comme paramètre "mettre les coordonné : "
    Reponse = input("mettre les coordonné : ")
    # si la variable Reponse n'est pas dans la liste "a1","a2","a3","A1","A2","A3","b1","b2","b3","B1","B2","B3","c1","c2","c3","C1","C2","C3"
    if not Reponse in ["a1","a2","a3","A1","A2","A3","b1","b2","b3","B1","B2","B3","c1","c2","c3","C1","C2","C3"]:
        # alors afficher "réponse incorectte"
        print("réponse inconrectte")
        # éxecuter la fonction coupJoueur
        coupJoueur()
    # sinon
    else:
        # afficher "bonne réponse"
        print("bonne réponse")
        # si la variable Reponse est égal a "a1" ou "A1"
        if Reponse == "a1" or Reponse == "A1":
            # alors si ligneUn[1] n'est pas égal a ""
            if ligneUn[1] != "":
                # alors afficher "yolo"
                print("yolo")
                # éxecuter coupJoueur
                coupJoueur()
            # si ligneUn[1] est égal a ""
            elif ligneUn[1] == "":
                # alors si la variable Jun est supérieur a la variable Jdeux
                if Jun > Jdeux :
                    # alors assigne a la variable ligneUn[1] est égal a "x"
                    ligneUn[1] ="x"
                # si la variable Jdeux est supérieur a la variable Jun
                elif Jdeux > Jun :
                    # alors assigne a la variable ligneUn[1] est égal a "o"
                    ligneUn[1] ="o"
            # sinon
            else:
                # afficher "erreur"
                print("erreur")
        # si la variable Reponse est égal a "b1" ou "B1"
        elif Reponse == "b1" or Reponse == "B1":
            # alors si ligneUn[2] n'est pas égal a ""
            if ligneUn[2] != "":
                # alors afficher "yolo"
                print("yolo")
                # éxecuter coupJoueur
                coupJoueur()
            # si ligneUn[2] est égal a ""
            elif ligneUn[2] == "":
                # alors si la variable Jun est supérieur a la variable Jdeux
                if Jun > Jdeux :
                    # alors assigne a la variable ligneUn[2] est égal a "x"
                    ligneUn[2] ="x"
                # si la variable Jdeux est supérieur a la variable Jun
                elif Jdeux > Jun :
                    # alors assigne a la variable ligneUn[2] est égal a "o"
                    ligneUn[2] ="o"
            # sinon
            else:
                # afficher "erreur"
                print("erreur")
        # si la variable Reponse est égal a "c1" ou "C1"
        elif Reponse == "c1" or Reponse == "C3":
            # alors si ligneUn[3] n'est pas égal a ""
            if ligneUn[3] != "":
                print("yolo")
                coupJoueur()
            elif ligneUn[3] == "":
                if Jun > Jdeux :
                    ligneUn[3] ="x"
                elif Jdeux > Jun :
                    ligneUn[3] ="o"
            else:
                print("erreur")
        # si la variable Reponse est égal a "a2" ou "A2"
        elif Reponse == "a2" or Reponse == "A2":
            if ligneDeux[1] != "":
                print("yolo")
                coupJoueur()
            elif ligneDeux[1] == "":
                if Jun > Jdeux :
                    ligneDeux[1] ="x"
                elif Jdeux > Jun :
                    ligneDeux[1] ="o"
            else:
                print("erreur")
        # si la variable Reponse est égal a "b2" ou "B2"
        elif Reponse == "b2" or Reponse == "B2":
            if ligneDeux[2] != "":
                print("yolo")
                coupJoueur()
            elif ligneDeux[2] == "":
                if Jun > Jdeux :
                    ligneDeux[2] ="x"
                elif Jdeux > Jun :
                    ligneDeux[2] ="o"
            else:
                print("erreur")
        elif Reponse == "c2" or Reponse == "C2":
            if ligneDeux[3] != "":
                print("yolo")
                coupJoueur()
            elif ligneDeux[3] == "":
                if Jun > Jdeux :
                    ligneDeux[3] ="x"
                elif Jdeux > Jun :
                    ligneDeux[3] ="o"
            else:
                print("erreur")
        elif Reponse == "a3" or Reponse == "A3":
            if ligneTrois[1] != "":
                print("yolo")
                coupJoueur()
            elif ligneTrois[1] == "":
                if Jun > Jdeux :
                    ligneTrois[1] ="x"
                elif Jdeux > Jun :
                    ligneTrois[1] ="o"
            else:
                print("erreur")
        elif Reponse == "b3" or Reponse == "B3":
            if ligneTrois[2] != "":
                print("yolo")
                coupJoueur()
            elif ligneTrois[2] == "":
                if Jun > Jdeux :
                    ligneTrois[2] ="x"
                elif Jdeux > Jun :
                    ligneTrois[2] ="o"
            else:
                print("erreur")
        elif Reponse == "c3" or Reponse == "C3":
            if ligneTrois[3] != "":
                print("yolo")
                coupJoueur()
            elif ligneTrois[3] == "":
                if Jun > Jdeux :
                    ligneTrois[3] ="x"
                elif Jdeux > Jun :
                    ligneTrois[3] ="o"
            else:
                print("erreur")
            
explication = 0
def StarterGame():    
    global explication
    if explication == 0:
        print("yo sale dino, je t'explique les règle ^^, :")
        print("le morpion, le joueur 1 c'est la croix, joueur 2 le rond, celui qui arrive a alligner dans le cube de 3 sur 3, 3 X ou 3 O a gagner")
        print("voila bon bonne chance !")
        explication = 1
    global Jun
    global Jdeux
    global gagnant
    global compteTour
    global encore
    global Tableau
    gagnant = 10
    print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
    while not gagnant in [0,1,2]:
        if not gagnant in [0,1,2]:
            Jun = Jdeux + 1
            coupJoueur()
            compteTour = compteTour + 1
            print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
            winner()
        if not gagnant in [0,1,2]:   
            Jdeux = Jun + 1
            coupJoueur()
            compteTour = compteTour + 1
            print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
            winner()
    if gagnant == 0:
        print("matche nul, vous êtes nul !")     
        Restart()
    elif gagnant == 1:
        print("joueur 1 (ps celui qui a les x ) est gagnant, ps le joueur 2 tes nul")
        Restart()
    elif gagnant == 2:
        print("le joueur 2 (ps celui qui a les o ) est gagnant, ps le joueur 1 tes nul")
        Restart()
        
            
StarterGame()