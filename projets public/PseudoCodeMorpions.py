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
# assigner a la variable ligneUn la liste ["1","","",""]
# assigner a la variable ligneDeux la liste ["2","","",""]
# assigner a la variable ligneTrois la liste ["3","","",""]
# initialiser la variable compteTour a 0
# initialiser la variable encore a 0

# assigner a la variable colonneUn la liste [ligneUn[1],ligneDeux[1],ligneTrois[1]]
# assigner a la variable colonneDeux la liste [ligneUn[2],ligneDeux[2],ligneTrois[2]]
# assigner a la variable colonneDeux la liste [ligneUn[3],ligneDeux[3],ligneTrois[3]]
# assigner a la variable diagoUn la liste [colonneUn[0],colonneDeux[1],colonneTrois[2]]
# assigner a la variable diagoDeux la liste [colonneUn[2],colonneDeux[1],colonneTrois[0]]

# initialiser la variable Jun a 0
# initialiser la variable Jdeux a 0
# initialiser la variable gagnant a 3
# assigner a la variable Tableau la liste [coordonne,ligneUn,ligneDeux,ligneTrois]

# definition de la fonction Restart
    # globaliser la variable ligneDeux
    # globaliser la variable ligneUn
    # globaliser la variable ligneTrois
    # globaliser la variable colonneDeux
    # globaliser la variable colonneUn
    # globaliser la variable colonneTrois
    # globaliser la variable diagoDeux
    # globaliser la variable diagoUn
    # globaliser la variable gagnant
    # globaliser la variable Jun
    # globaliser la variable Jdeux
    # globaliser la variable compteTour
    # globaliser la variable encore
    # globaliser la variableT Tableau
    # affiche "yo bande de débile tu veux retenter ?"
    # assigne a la variable encore le retour d'éxecutien de la fonction input de paramètre "-1 = retenter || -2 = j'abandone car jsui nul: "
    # si la variable encore n'est pas dans la liste ['1','2']
        # alors afficher "te fous pas dma geu ptit batard mes 1 ou 2 et pas : ",encore
        # afficher "yo bande de débile vous voulez retenter ?"
        # éxécute la fonction Restart
    # si la variable encore est dans la liste ['1','2']
        # alors si la variable encore est = a 1
            # alors afficher "oki Dinosaure ON RESTARTTTTTTTRE"
            # assigne a la variable coordone la liste ['',"A","B","C"]
            # assigne a la variable ligneUn la liste ["1","","",""]
            # assigne a la variable ligneDeux la liste ["2","","",""]
            # assigne a la variable ligneTrois la liste ["3","","",""]
            # réinitializer a la variable compteTour a 0
            # réinitializer a la variable encore a 0
            # assigne a la variable colonneUn la liste [ligneUn[1],ligneDeux[1],ligneTrois[1]]
             # assigne a la variable colonneDeux la liste [ligneUn[2],ligneDeux[2],ligneTrois[2]]
             # assigne a la variable colonneTrois la liste [ligneUn[3],ligneDeux[3],ligneTrois[3]]
             # assigne a la variable diagoUn la liste [colonneUn[0],colonneDeux[1],colonneTrois[2]]
             # assigne a la variable diagoDeux la liste [colonneUn[2],colonneDeux[1],colonneTrois[0]]
            # réinitialize la variable Jun a 0
            # réinitialize la variable Jdeux a 0
            # réinitialize la variable gagnant a 3
            # assigne a la variable Tableau la liste [coordonne,ligneUn,ligneDeux,ligneTrois]
            # éxecute la fonction StarterGame
        # si la variable encore = a 2
            # alors afficher "NNNNNNNNNNNNNNOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOBBBBBBBBBBBBBB"
            # retourne la fonction
# definir la fonction winner
    # globaliser la variable ligneDeux
    # globaliser la variable ligneUn
    # globaliser la variable ligneTrois
    # globaliser la variable colonneDeux
    # globaliser la variable colonneUn
    # globaliser la variable colonneTrois
    # globaliser la variable diagoDeux
    # globaliser la variable diagoUn
    # globaliser la variable gagnant
    # assigne a la variable colonneUn la liste [ligneUn[1],ligneDeux[1],ligneTrois[1]]
    # assigne a la variable colonneDeux la liste [ligneUn[2],ligneDeux[2],ligneTrois[2]]
    # assigne a la variable colonneTrois la liste [ligneUn[3],ligneDeux[3],ligneTrois[3]]
    # assigne a la variable diagoUn la liste [colonneUn[0],colonneDeux[1],colonneTrois[2]]
    # assigne a la variable diagoDeux la liste [colonneUn[2],colonneDeux[1],colonneTrois[0]]
    # si la variable ligneUn[1], ligneUn[2], ligneUn[3] est égal a x
        # alors assigner a la variable gagnant, 1
    # si la variable ligneDeux[1], ligneDeux[2], ligneDeux[3] est égal a x
        # alors assigner a la variable gagnant, 1
    # si la variable ligneTrois[1], ligneTrois[2], ligneTrois[3] est égal a x
        # alors assigner a la variable gagnant, 1
    # si la variable colonneUn[0], colonneUn[1], colonneUn[2] est égal a x
        # alors assigner a la variable gagnant, 1
    # si la variable colonneDeux[0], colonneDeux[1], colonneDeux[2] est égal a x
        # alors assigner a la variable gagnant, 1
    # si la variable colonneTrois[0], colonneTrois[1], colonneTrois[2] est égal a x
        # alors assigner a la variable gagnant, 1
    # si la variable diagoUn[0], diagoUn[1], diagoUn[2] est égal a x
        # alors assigner a la variable gagnant, 1
    # si la variable diagoDeux[0], diagoDeux[1], diagoDeux[2] est égal a x
        # alors assigner a la variable gagnant, 1
    # si la variable ligneUn[1], ligneUn[2], ligneUn[3] est égal a o
        # alors assigne a la variable gagnant, 2
    # si la variable ligneDeux[1], ligneDeux[2], ligneDeux[3] est égal a o
        # alors assigne a la variable gagnant, 2
    # si la variable ligneTrois[1], ligneTrois[2], ligneTrois[3] est égal a o
        # alors assigne a la variable gagnant, 2
    # si la variable colonneUn[0], colonneUn[1], colonneUn[2] est égal a o
        # alors assigne a la variable gagnant, 2
    # si la variable colonneDeux[0], colonneDeux[1], colonneDeux[2] est égal a o
        # alors assigne a la variable gagnant, 2
    # si la variable colonneTrois[0], colonneTrois[1], colonneTrois[2] est égal a o
        # alors assigne a la variable gagnant, 2
    # si la variable diagoUn[0], diagoUn[1], diagoUn[2] est égal a o
        # alors assigne a la variable gagnant, 2
    # si la variable diagoDeux[0], diagoDeux[1], diagoDeux[2] est égal a o
        # alors assigne a la variable gagnant, 2
    # si compteTour est égal a 9
        # alors assigne a la variable gagnant, 0
# definir la fonction coupJoueur
    # globaliser la variable ligneDeux
    # globaliser la variable ligneUn
    # globaliser la variable ligneTrois
    # globaliser la variable colonneDeux
    # globaliser la variable colonneUn
    # globaliser la variable colonneTrois
    # globaliser la variable diagoDeux
    # globaliser la variable diagoUn
    # globaliser la variable gagnant
    # assigner a la variable reponse, le retour de l'éxecution de la fonction input avec comme paramètre "mettre les coordonné : "
    # si la variable Reponse n'est pas dans la liste "a1","a2","a3","A1","A2","A3","b1","b2","b3","B1","B2","B3","c1","c2","c3","C1","C2","C3"
        # alors afficher "réponse incorectte"
        # éxecuter la fonction coupJoueur
    # sinon
        # afficher "bonne réponse"
        # si la variable Reponse est égal a "a1" ou "A1"
            # alors si ligneUn[1] n'est pas égal a ""
                # alors éxecuter coupJoueur
            # si ligneUn[1] est égal a ""
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneUn[1] est égal a "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneUn[1] est égal a "o"
            # sinon
                # afficher "erreur"
        # si la variable Reponse est égal a "b1" ou "B1"
            # alors si ligneUn[2] n'est pas égal a ""
                # alors éxecuter coupJoueur
            # si ligneUn[2] est égal a ""
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneUn[2] est égal a "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneUn[2] est égal a "o"
            # sinon
                # afficher "erreur"
        # si la variable Reponse est égal a "c1" ou "C1"
            # alors si ligneUn[3] n'est pas égal a ""
                # alors éxecute coupJoueur
            # si la varibale ligneUn[3] est égal a rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneUn[3] "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneUn "o"
            # sinon
                # afficher "erreur"
        # si la variable Reponse est égal a "a2" ou "A2"
            # alors si la variable ligneDeux[1] n'est pas égal a rien
                # alors éxecute coupJoueur
            # si la variable ligneDeux[1] est égal a rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneDeux[1] est égal a "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneDeux[1] est égal a "o"
            # sinon
        # si la variable Reponse est égal a "b2" ou "B2"
            # alors si la variable ligneDeux[2] n'est pas égal a rien
                # alors éxecute coupJoueur
            # si la variable ligneDeux[2] est égal a rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneDeux[2] est égal a "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneDeux[2] est égal a "o"
            # sinon
                # alors affiche "erreur"
        # si la variable Reponse est égal a "c2" ou "C2" 
            # alors si la variable ligneDeux[3] n'est pas égal a rien
                # alors éxecute coupJoueur
            # si la variable ligneDeux[3] est égal a rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneDeux[3] est égal a "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneDeux[3] est égal a "o"
            # sinon
        # si la variable Reponse est égal a "a3" ou "A3"
            # alors si la variable ligneTrois[1] n'est pas égal à rien
                # alors éxecute coupJoueur
            # si la variable ligneTrois[1] est égal rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneTrois[1] "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneTrois[1] "o"
            # sinon
                # affiche "erreur"
        # si la variable Reponse est égal a "b3" ou "B3"
            # alors si la variable ligneTrois[2] n'est pas égal à rien
                # alors éxecute coupJoueur
            # si la variable ligneTrois[2] est égal rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneTrois[2] "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneTrois[2] "o"
            # sinon
                # affiche "erreur"
        # si la variable Reponse est égal a "c3" ou "C3"
            # alors si la variable ligneTrois[3] n'est pas égal à rien
                # alors éxecute coupJoueur
            # si la variable ligneTrois[3] est égal rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneTrois[3] "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneTrois[3] "o"
            # sinon
                # affiche "erreur"

# initialiser la variable explication a 0
# définir la fonction StarterGame
    # globaliser la variable explication
    # si la variable explication est égal a 0
        # alors afficher "yo sale dino, je t'explique les règle ^^, :"
        # afficher "le morpion, le joueur 1 c'est la croix, joueur 2 le rond, celui qui arrive a alligner dans le cube de 3 sur 3, 3 X ou 3 O a gagner"
        # afficher "voila bon bonne chance !"
        # assigner a la variable explication 1
    
    # globaliser la variable gagnant
    # globaliser la variable Jun
    # globaliser la variable Jdeux
    # globaliser la variable compteTour
    # globaliser la variable encore
    # globaliser la variableT Tableau
    # initialise la cariable gagnant 10
    # afficher la variable tableau
    # tant que la variable gagnant n'est pas dans la liste [0,1,2]
        # si la variable gagnant n'est pas dans la liste [0,1,2]
            # alors assigne a la variable Jun, la variable Jdeux + 1
            # éxecute coupJoueur
            # assigne a la variable compteTour, la variable compteTour + 1
            # affiche Tableau
            # éxecute winner
        # si la variable gagnant n'est pas dans la liste [0,1,2]
            # alors assigne a la variable Jdeux, la variable Jun + 1
            # éxecute coupJoueur
            # assigne a la variable compteTour, la variable compteTour + 1
            # affiche Tableau
            # éxecute winner
    # Si la variable gagnant est égal a 0
        # alors affiche "matche nul, vous êtes nul !"
        # éxecute la fonction Restart  
    # si la variable gagnant est égal 1
        # alors affiche "joueur 1 (ps celui qui a les x ) est gagnant, ps le joueur 2 tes nul"
        # éxecute la fonction Restart
    # si la variable gagnant est égal 2
        # alors affiche "joueur 2 (ps celui qui a les o ) est gagnant, ps le joueur 1 tes nul"
        # éxecute la fonction Restart
        
# éxecute la fonction StarterGame
