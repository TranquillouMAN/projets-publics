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
    # globaliser la variable afm
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
            # initialiser la variable afm a 0
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
        # si la variable Reponse est égal a "a1" ou "A1" ou "1A"
            # alors si ligneUn[1] n'est pas égal a ""
                # alors éxecuter coupJoueur
            # si ligneUn[1] est égal a ""
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneUn[1] est égal a "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneUn[1] est égal a "o"
            # sinon
                # afficher "erreur"
        # si la variable Reponse est égal a "b1" ou "B1" ou "1B"
            # alors si ligneUn[2] n'est pas égal a ""
                # alors éxecuter coupJoueur
            # si ligneUn[2] est égal a ""
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneUn[2] est égal a "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneUn[2] est égal a "o"
            # sinon
                # afficher "erreur"
        # si la variable Reponse est égal a "c1" ou "C1" ou "1C"
            # alors si ligneUn[3] n'est pas égal a ""
                # alors éxecute coupJoueur
            # si la varibale ligneUn[3] est égal a rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneUn[3] "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneUn "o"
            # sinon
                # afficher "erreur"
        # si la variable Reponse est égal a "a2" ou "A2" ou "2A"
            # alors si la variable ligneDeux[1] n'est pas égal a rien
                # alors éxecute coupJoueur
            # si la variable ligneDeux[1] est égal a rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneDeux[1] est égal a "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneDeux[1] est égal a "o"
            # sinon
        # si la variable Reponse est égal a "b2" ou "B2" ou "2B"
            # alors si la variable ligneDeux[2] n'est pas égal a rien
                # alors éxecute coupJoueur
            # si la variable ligneDeux[2] est égal a rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneDeux[2] est égal a "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneDeux[2] est égal a "o"
            # sinon
                # alors affiche "erreur"
        # si la variable Reponse est égal a "c2" ou "C2" ou "2C"
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
        # si la variable Reponse est égal a "b3" ou "B3" ou "3B"
            # alors si la variable ligneTrois[2] n'est pas égal à rien
                # alors éxecute coupJoueur
            # si la variable ligneTrois[2] est égal rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneTrois[2] "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneTrois[2] "o"
            # sinon
                # affiche "erreur"
        # si la variable Reponse est égal a "c3" ou "C3" ou "3C"
            # alors si la variable ligneTrois[3] n'est pas égal à rien
                # alors éxecute coupJoueur
            # si la variable ligneTrois[3] est égal rien
                # alors si la variable Jun est supérieur a la variable Jdeux
                    # alors assigne a la variable ligneTrois[3] "x"
                # si la variable Jdeux est supérieur a la variable Jun
                    # alors assigne a la variable ligneTrois[3] "o"
            # sinon
                # affiche "erreur"
# initialiser la variable afm a 0
# définir la fonction Bot
    # globaliser la variable ligneDeux
    # globaliser la variable ligneUn
    # globaliser la variable ligneTrois
    # globaliser la variable colonneDeux
    # globaliser la variable colonneUn
    # globaliser la variable colonneTrois
    # globaliser la variable diagoDeux
    # globaliser la variable diagoUn
    # globaliser la variable gagnant
    # globaliser la variable Tableau
    # globaliser la variable compteTour
    # globaliser la variable afm
    # assigne a la variable TableauRobot la liste [ligneUn[1],ligneUn[2],ligneUn[3],ligneDeux[1],ligneDeux[2],ligneDeux[3],ligneTrois[1],ligneTrois[2],ligneTrois[3]]
    # assigne a la variable colonneUn la liste [ligneUn[1],ligneDeux[1],ligneTrois[1]]
    # assigne a la variable colonneDeux la liste [ligneUn[2],ligneDeux[2],ligneTrois[2]]
    # assigne a la variable colonneTrois la liste [ligneUn[3],ligneDeux[3],ligneTrois[3]]
    # assigne a la variable diagoUn la liste [colonneUn[0],colonneDeux[1],colonneTrois[2]]
    # assigne a la variable diagoDeux la liste [colonneUn[2],colonneDeux[1],colonneTrois[0]]
    # si la variable afm est égal 0
        # si la variable ligneUn[1] est égal a 'x' ou, la variable ligneUn[3] est égal a 'x' ou la variable ligneTrois[1] est égal a 'x' ou la variable ligneTrois[3] est égal a 'x'
            # alors assigne a la variable ligneDeux[2] 'o'
            # assigne a la varibale afm = 1
            # retourne la fonction
        # si la variable ligneDeux[2] est égal a 'x'
            # alors assigne a la variable ligneUn[1] 'o'
            # assigne a la variable afm 1
            # retourne la fonction 
        # si la variable ligneUn[2] est égal a 'x'
            # alors assigne a la variable ligneDeux[2] 'o'
            # assigne la variable afm 1
            # retourne la fonction
        # si la variable ligneDeux[1] est égal a 'x'
            # alors assigne a la variable ligneDeux[2] 'o'
            # assigne la variable afm 1
            # retourne la fonction
        # si la variable ligneTrois[2] est égal a 'x'
            # alors assigne a la variable ligneDeux[2] 'o'
            # assigne la variable afm 1
            # retourne la fonction
        # si la variable ligneDeux[3] est égal a 'x'
            # alors assigne a la variable ligneDeux[2] 'o'
            # assigne la variable afm 1
            # retourne la fonction
    # si la variable afm est égal a 1
        # pour la variable i dans la variable TableauRobot
            # si la variable i est égal a rien
                # alors si la variable ligneUn.count('o') est égal a 2
                    # alors alors pour i dans l'intervale (1, len(ligneUn))
                        # si la variable ligneUn[i] est égal a rien
                            # alors assigne a la variable ligneUn[i] 'o'
                            # retourner la fonction
                # si la variable ligneDeux.count('o') est égal a 2
                    # alors pour i dans l'intervale (1, len(ligneDeux))
                        # si la variable ligneDeux[i] est égal a rien
                            # alors assigne a la variable ligneDeux[i] 'o'
                            # retourner la fonction
                # si la variable ligneTrois.count('o') est égal a 2
                    # alors pour i dans l'intervale (1, len(ligneTrois))
                        # si la variable ligneTrois[i] est égal a rien
                            # alors assigne a la variable ligneTrois[i] 'o'
                            # retourner la fonction
                # si la variable colonneUn.count('o') est égal a 2
                    # alors alors pour i dans l'ensemble (len(colonneUn))
                        # si la variable colonneUn[i] est égal a rien
                            # alors assigne a la variable colonneUn[i] 'o'
                            # assigne a la variable ligneUn[1] colonneUn[0]; a la variable ligneDeux[1] colonneUn[1]; a la variable ligneTrois[1] colonneUn[2]
                            # retourner la fonction
                # si la variable colonneDeux.count('o') est égal a 2
                    # alors pour i dans l'ensemble (len(colonneDeux))
                        # si la variable colonneDeux[i] est égal a rien
                            # alors assigne a la variable colonneDeux[i] 'o'
                            # assigne a la variable ligneUn[2] colonneDeux[0]; a la variable ligneDeux[2] colonneDeux[1]; a la variable ligneTrois[2] colonneUn[2]
                            # retourner la fonction
                # si la variable colonneTrois.count('o') est égal a 2
                    # alors pour i dans l'ensemble (len(colonneTrois))
                        # si la variable colonneTrois[i] est égal a rien
                            # alors assigne a la variable colonneTrois[i] 'o'
                            # assigne a la variable ligneUn[3] colonneTrois[0]; a la variable ligneDeux[3] colonneTrois[1]; a la variable ligneTrois[3] colonneTrois[2]
                            # retourner la fonction
                # si la variable diagoUn.count('o') est égal a 2
                    # alors pour i dans l'ensemble (len(diagoUn))
                        # si la variable diagoUn[i] est égal a rien
                            # alors assigne a la variable diagoUn[i] 'o'
                            # assigne a la variable ligneUn[1] diagoUn[0]; a la variable ligneDeux[2] diagoUn[1]; a la variable ligneTrois[3] diagoUn[2]
                            # retourner la fonction
                # si la variable diagoDeux.count('o') est égal a 2
                    # alors pour i dans l'ensemble (len(diagoDeux))
                        # si la variable diagoDeux[i] est égal a rien
                            # alors assigne a la variable diagoDeux[i] 'o'
                            # assigne a la variable ligneUn[3] diagoDeux[0]; a la variable ligneDeux[2] diagoDeux[1]; a la variable ligneTrois[1] diagoDeux[0]
                            # retourner la fonction
                # si la variable ligneUn.count('') est supérieur ou égal a 1
                    # alors si la variable ligneUn.count('x') est égal a 2
                        # alors alors pour i dans l'intervale (1, len(ligneUn))
                            # si la variable ligneUn[i] est égal a rien
                                # alors assigne a la variable ligneUn[i] 'o'
                                # retourner la fonction
                # si la variable ligneDeux.count('') est supérieur ou égal a 1
                    # alors si la variable ligneDeux.count('x') est égal a 2             
                        # alors pour i dans l'intervale (1, len(ligneDeux))
                            # si la variable ligneDeux[i] est égal a rien
                                # alors assigne a la variable ligneDeux[i] 'o'
                                # retourner la fonction
                # si la variable ligneTrois.count('') est supérieur ou égal a 1
                    # alors si la variable ligneTrois.count('x') est égal a 2
                        # alors pour i dans l'intervale (1, len(ligneTrois))
                            # si la variable ligneTrois[i] est égal a rien
                                # alors assigne a la variable ligneTrois[i] 'o'
                                # retourner la fonction
                # si la variable colonneUn.count('') est supérieur ou égal a 1
                    # alors si la variable colonneUn.count('x') est égal a 2
                        # alors alors pour i dans l'ensemble (len(colonneUn))
                            # si la variable colonneUn[i] est égal a rien
                                # alors assigne a la variable colonneUn[i] 'o'
                                # assigne a la variable ligneUn[1] colonneUn[0]; a la variable ligneDeux[1] colonneUn[1]; a la variable ligneTrois[1] colonneUn[2]
                                # retourner la fonction
                # si la variable colonneDeux.count('') est supérieur ou égal a 1
                    # alors si la variable colonneDeux.count('x') est égal a 2             
                        # alors pour i dans l'ensemble (len(colonneDeux))
                            # si la variable colonneDeux[i] est égal a rien
                                # alors assigne a la variable colonneDeux[i] 'o'
                                # assigne a la variable ligneUn[2] colonneDeux[0]; a la variable ligneDeux[2] colonneDeux[1]; a la variable ligneTrois[2] colonneDeux[2]
                                # retourner la fonction
                # si la variable colonneTrois.count('') est supérieur ou égal a 1
                    # alors si la variable colonneTrois.count('x') est égal a 2
                        # alors pour i dans l'ensemble (len(colonneTrois))
                            # si la variable colonneTrois[i] est égal a rien
                                # alors assigne a la variable colonneTrois[i] 'o'
                                # assigne a la variable ligneUn[3] colonneTrois[0]; a la variable ligneDeux[3] colonneTrois[1]; a la variable ligneTrois[3] colonneTrois[2]
                                # retourner la fonction
                # si la variable diagoUn.count('') est supérieur ou égal a 1
                    # alors si la variable diagoUn.count('x') est égal a 2        
                        # alors pour i dans l'ensemble (len(diagoUn))
                            # si la variable diagoUn[i] est égal a rien
                                # alors assigne a la variable diagoUn[i] 'o'
                                # assigne a la variable ligneUn[1] diagoUn[0]; a la variable ligneDeux[2] diagoUn[1]; a la variable ligneTrois[3] diagoUn[2]
                                # retourner la fonction
                # si la variable diagoDeux.count('') est supérieur ou égal a 1
                    # alors si la variable diagoDeux.count('x') est égal a 2
                        # alors pour i dans l'ensemble (len(diagoDeux))
                            # si la variable diagoDeux[i] est égal a rien
                                # alors assigne a la variable diagoDeux[i] 'o'
                                # assigne a la variable ligneUn[3] diagoDeux[2]; a la variable ligneDeux[2] diagoDeux[1]; a la variable ligneTrois[1] diagoDeux[0]
                                # retourner la fonction
                # si la variable ligneUn[1] et ligneTrois[3] est égal a 'x'
                    # alors si la variable ligneUn[2] est égal a rien
                        # alors assigne a la variable ligneUn[2] 'o'
                        # retourner la fonction
                # si la variable ligneUn[3] et ligneTrois[1] est égal a 'x'
                    # alors si la variable ligneUn[2] est égal a rien
                        # alors assigne a la variable ligneUn[2] 'o'
                        # retourner la fonction
                # si la variable ligneDeux[2] et ligneTrois[3] est égal a 'x'
                    # alors si la variable ligneTrois[1] est égal a rien
                        # alors assigne a la variable ligneTrois[1] 'o'
                        # retourner la fonction
                # si la variable ligneDeux[2] et ligneTrois[1] est égal a 'x'
                    # alors si la variable ligneUn[3] est égal a rien
                        # alors assigne a la variable ligneUn[3] 'o'
                        # retourner la fonction
                # si la variable ligneDeux[2] et ligneUn[3] est égal a 'x'
                    # alors si la variable ligneTrois[1] est égal a rien
                        # alors assigne a la variable ligneTrois[1] 'o'
                        # retourner la fonction
                # si la variable ligneTrois[1] et ligneDeux[2] est égal a 'x'
                    # alors si la variable ligneUn[3] est égal a rien
                        # alors assigne a la variable ligneTrois[3] 'o'
                        # retourner la fonction
                # si la variable ligneTrois[2] est égal a 'x'
                    # alors si la variable ligneUn[3] ou la variable ligneUn[1] est égal a x
                        # alors si la variable ligneTrois[3] est égal a rien
                            # alors assigne a la variable ligneTrois[3] 'o'
                            # retourner la fonction
                # si la variable ligneUn[2] est égal a 'x'
                    # alors si la variable ligneUn[3] ou la variable ligneUn[1] est égal a x
                        # alors si la variable ligneUn[3] est égal a rien
                            # alors assigne a la variable ligneDeux[3] 'o'
                            # retourner la fonction
                # si la variable diagoUn.count('o') est égal a 1
                    # alors alors pour la variable i dans la range(len(diagoUn))
                        # si la variable diagoUn[i] est égal a rien
                            # alors assigne a la variable diagoUn[i] 'o'
                            # assigne a la variable ligneUn[1] diagoUn[0]; a la variable ligneDeux[2] diagoUn[1]; a la variable ligneTrois[3] diagoUn[2]
                            # retourner la fonction
                # si la variable diagoDeux.count('o') est égal a 1
                    # alors pour la variable i dans la range(len(diagoDeux))
                        # si la variable diagoDeux[i] est égal a rien
                            # alors assigne a la variable diagoDeux[i] 'o'
                            # assigne a la variable ligneUn[3] diagoDeux[2]; a la variable ligneDeux[2] diagoDeux[1]; a la variable ligneTrois[1] diagoDeux[0]
                            # retourner la fonction
                # si la variable ligneUn.count('o') est égal a 1         
                    # alors pour la variable i dans la range(len(ligneUn))
                        # si la variable ligneUn[i] est égal a rien
                            # alors assigne a la variable ligneUn[i] 'o'
                            # retourner la fonction
                # si la variable ligneDeux.count('o') est égal a 1
                    # alors pour la variable i dans la range(len(ligneDeux))
                        # si la variable ligneDeux[i] est égal a rien
                            # alors assigne a la variable ligneDeux[i] 'o'
                            # retourner la fonction
                # si la variable ligneTrois.count('o') est égal a 1
                    # alors pour la variable i dans la range(len(ligneTrois))
                        # si la variable ligneTrois[i] est égal a rien
                            # alors assigne a la variable ligneTrois[i] 'o'
                            # retourner la fonction
                # si la variable colonneUn.count('o') est égal a 1
                    # alors pour la variable i dans la range(len(colonneUn))
                        # si la variable colonneUn[i] est égal a rien
                            # alors assigne a la variable colonneUn[i] 'o'
                            # assigne a la variable ligneUn[1] colonneUn[0]; a la variable ligneDeux[1] colonneUn[1]; a la variable ligneTrois[1] colonneUn[2]
                            # retourner la fonction
                # si la variable colonneDeux.count('o') est égal a 1
                    # alors pour la variable i dans la range(len(colonneDeux))
                        # si la variable colonneDeux[i] est égal a rien
                            # alors assigne a la variable colonneDeux[i] 'o'
                            # assigne a la variable ligneUn[2] colonneDeux[0]; a la variable ligneDeux[2] colonneDeux[1]; a la variable ligneTrois[2] colonneDeux[2]
                            # retourner la fonction
                # si la variable colonneTrois.count('o') est égal a 1
                    # alors pour la variable i dans la range(len(colonneTrois))
                        # si la variable colonneTrois[i] est égal a rien
                            # alors assigne a la variable colonneTrois[i] 'o'
                            # assigne a la variable ligneUn[3] colonneTrois[0]; a la variable ligneDeux[3] colonnetrois[1]; a la variable ligneTrois[3] colonneTrois[2]
                            # retourner la fonction

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
    # initialise la variable gagnant 3
    # afficher "me revoila tu veux te taper contre qui ? le bot ou un pote ?"
    # afficher "réponse possible : "
    # afficher "-bot" et "-pote"
    # assigne a la variable demande "Restart"
    # assigne a la variable demande, le retour de l'execution de la fonction input de paramètre "votre choix: "
    # si la variable demande n'est pas dans la liste ["bot","pote"]
        # alors afficher "tu me mes roublise, stp mes une valeur possible pas :",demande
        # éxecuter la fonction StarterGame
    # si la variable demande est dans la liste ["bot","pote"]
        # alors si la variable demande est égal a "pote"
            # afficher Tableau
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
        # si la variable demande est égal a "bot"
            # afficher Tableau
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
