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
    # globaliser la variable afm
    global afm
    # affiche "yo bande de d??bile tu veux retenter ?"
    print("yo bande de d??bile tu veux retenter ?")
    # assigne a la variable encore le retour d'??xecutien de la fonction input de param??tre "-1 = retenter || -2 = j'abandone car jsui nul: "
    encore = input("-1 = retenter || -2 = j'abandone car jsui nul: ")
    # si la variable encore n'est pas dans la liste ['1','2']
    if not encore in ['1','2']:
        # alors afficher "te fous pas dma geu ptit batard mes 1 ou 2 et pas : ",encore
        print("te fous pas dma geu ptit batard mes 1 ou 2 et pas : ",encore)
        # afficher "yo bande de d??bile vous voulez retenter ?"
        print("yo bande de d??bile vous voulez retenter ?")
        # ??x??cute la fonction Restart
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
            # r??initializer a la variable compteTour a 0
            compteTour = 0
            # r??initializer a la variable encore a 0
            encore = 0
            # initialiser la variable afm a 0
            afm = 0
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
            # r??initialize la variable Jun a 0
            Jun = 0
            # r??initialize la variable Jdeux a 0
            Jdeux = 0
            # r??initialize la variable gagnant a 3
            gagnant = 3
            # assigne a la variable Tableau la liste [coordonne,ligneUn,ligneDeux,ligneTrois]
            Tableau = [coordonne,ligneUn,ligneDeux,ligneTrois]
            # ??xecute la fonction StarterGame
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
    # si la variable ligneUn[1], ligneUn[2], ligneUn[3] est ??gal a x
    if ligneUn[1] == "x" and ligneUn[2] == "x" and ligneUn[3] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable ligneDeux[1], ligneDeux[2], ligneDeux[3] est ??gal a x
    elif ligneDeux[1] == "x" and ligneDeux[2] == "x" and ligneDeux[3] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable ligneTrois[1], ligneTrois[2], ligneTrois[3] est ??gal a x
    elif ligneTrois[1] == "x" and ligneTrois[2] == "x" and ligneTrois[3] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable colonneUn[0], colonneUn[1], colonneUn[2] est ??gal a x
    elif colonneUn[0] == "x" and colonneUn[1] == "x" and colonneUn[2] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable colonneDeux[0], colonneDeux[1], colonneDeux[2] est ??gal a x
    elif colonneDeux[0] == "x" and colonneDeux[1] == "x" and colonneDeux[2] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable colonneTrois[0], colonneTrois[1], colonneTrois[2] est ??gal a x
    elif colonneTrois[0] == "x" and colonneTrois[1] == "x" and colonneTrois[2] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable diagoUn[0], diagoUn[1], diagoUn[2] est ??gal a x
    elif diagoUn[0] == "x" and diagoUn[1] == "x" and diagoUn[2] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable diagoDeux[0], diagoDeux[1], diagoDeux[2] est ??gal a x
    elif diagoDeux[0] == "x" and diagoDeux[1] == "x" and diagoDeux[2] == "x":
        # alors assigner a la variable gagnant, 1
        gagnant = 1
    # si la variable ligneUn[1], ligneUn[2], ligneUn[3] est ??gal a o
    elif ligneUn[1] == "o" and ligneUn[2] == "o" and ligneUn[3] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable ligneDeux[1], ligneDeux[2], ligneDeux[3] est ??gal a o
    elif ligneDeux[1] == "o" and ligneDeux[2] == "o" and ligneDeux[3] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable ligneTrois[1], ligneTrois[2], ligneTrois[3] est ??gal a o
    elif ligneTrois[1] == "o" and ligneTrois[2] == "o" and ligneTrois[3] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable colonneUn[0], colonneUn[1], colonneUn[2] est ??gal a o
    elif colonneUn[0] == "o" and colonneUn[1] == "o" and colonneUn[2] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable colonneDeux[0], colonneDeux[1], colonneDeux[2] est ??gal a o
    elif colonneDeux[0] == "o" and colonneDeux[1] == "o" and colonneDeux[2] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable colonneTrois[0], colonneTrois[1], colonneTrois[2] est ??gal a o
    elif colonneTrois[0] == "o" and colonneTrois[1] == "o" and colonneTrois[2] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable diagoUn[0], diagoUn[1], diagoUn[2] est ??gal a o
    elif diagoUn[0] == "o" and diagoUn[1] == "o" and diagoUn[2] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si la variable diagoDeux[0], diagoDeux[1], diagoDeux[2] est ??gal a o
    elif diagoDeux[0] == "o" and diagoDeux[1] == "o" and diagoDeux[2] == "o":
        # alors assigne a la variable gagnant, 2
        gagnant = 2
    # si compteTour est ??gal a 9
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
    # assigner a la variable reponse, le retour de l'??xecution de la fonction input avec comme param??tre "mettre les coordonn?? : "
    Reponse = input("mettre les coordonn?? : ")
    # si la variable Reponse n'est pas dans la liste "a1","a2","a3","A1","A2","A3","b1","b2","b3","B1","B2","B3","c1","c2","c3","C1","C2","C3"
    if not Reponse in ["a1","a2","a3","A1","A2","A3","b1","b2","b3","B1","B2","B3","c1","c2","c3","C1","C2","C3"]:
        # alors afficher "r??ponse incorectte"
        print("r??ponse inconrectte")
        # ??xecuter la fonction coupJoueur
        coupJoueur()
    # sinon
    else:
        # afficher "bonne r??ponse"
        print("bonne r??ponse")
        # si la variable Reponse est ??gal a "a1" ou "A1" ou "1A"
        if Reponse == "a1" or Reponse == "A1" or Reponse =="1A":
            # alors si ligneUn[1] n'est pas ??gal a ""
            if ligneUn[1] != "":
                # alors ??xecuter coupJoueur
                coupJoueur()
            # si ligneUn[1] est ??gal a ""
            elif ligneUn[1] == "":
                # alors si la variable Jun est sup??rieur a la variable Jdeux
                if Jun > Jdeux :
                    # alors assigne a la variable ligneUn[1] est ??gal a "x"
                    ligneUn[1] ="x"
                # si la variable Jdeux est sup??rieur a la variable Jun
                elif Jdeux > Jun :
                    # alors assigne a la variable ligneUn[1] est ??gal a "o"
                    ligneUn[1] ="o"
            # sinon
            else:
                # afficher "erreur"
                print("erreur")
        # si la variable Reponse est ??gal a "b1" ou "B1" ou "1B"
        elif Reponse == "b1" or Reponse == "B1" or Reponse == "1B":
            # alors si ligneUn[2] n'est pas ??gal a ""
            if ligneUn[2] != "":
                # alors ??xecuter coupJoueur
                coupJoueur()
            # si ligneUn[2] est ??gal a ""
            elif ligneUn[2] == "":
                # alors si la variable Jun est sup??rieur a la variable Jdeux
                if Jun > Jdeux :
                    # alors assigne a la variable ligneUn[2] est ??gal a "x"
                    ligneUn[2] ="x"
                # si la variable Jdeux est sup??rieur a la variable Jun
                elif Jdeux > Jun :
                    # alors assigne a la variable ligneUn[2] est ??gal a "o"
                    ligneUn[2] ="o"
            # sinon
            else:
                # afficher "erreur"
                print("erreur")
        # si la variable Reponse est ??gal a "c1" ou "C1" ou "1C"
        elif Reponse == "c1" or Reponse == "C3" or Reponse == "1C":
            # alors si ligneUn[3] n'est pas ??gal a ""
            if ligneUn[3] != "":
                # alors ??xecute coupJoueur
                coupJoueur()
            # si la varibale ligneUn[3] est ??gal a rien
            elif ligneUn[3] == "":
                # alors si la variable Jun est sup??rieur a la variable Jdeux
                if Jun > Jdeux :
                    # alors assigne a la variable ligneUn[3] "x"
                    ligneUn[3] ="x"
                # si la variable Jdeux est sup??rieur a la variable Jun
                elif Jdeux > Jun :
                    # alors assigne a la variable ligneUn "o"
                    ligneUn[3] ="o"
            # sinon
            else:
                # afficher "erreur"
                print("erreur")
        # si la variable Reponse est ??gal a "a2" ou "A2" ou "2A"
        elif Reponse == "a2" or Reponse == "A2" or Reponse =="2A":
            # alors si la variable ligneDeux[1] n'est pas ??gal a rien
            if ligneDeux[1] != "":
                # alors ??xecute coupJoueur
                coupJoueur()
            # si la variable ligneDeux[1] est ??gal a rien
            elif ligneDeux[1] == "":
                # alors si la variable Jun est sup??rieur a la variable Jdeux
                if Jun > Jdeux :
                    # alors assigne a la variable ligneDeux[1] est ??gal a "x"
                    ligneDeux[1] ="x"
                # si la variable Jdeux est sup??rieur a la variable Jun
                elif Jdeux > Jun :
                    # alors assigne a la variable ligneDeux[1] est ??gal a "o"
                    ligneDeux[1] ="o"
            # sinon
            else:
                print("erreur")
        # si la variable Reponse est ??gal a "b2" ou "B2" ou "2B"
        elif Reponse == "b2" or Reponse == "B2" or Reponse == "2B":
            # alors si la variable ligneDeux[2] n'est pas ??gal a rien
            if ligneDeux[2] != "":
                # alors ??xecute coupJoueur
                coupJoueur()
            # si la variable ligneDeux[2] est ??gal a rien
            elif ligneDeux[2] == "":
                # alors si la variable Jun est sup??rieur a la variable Jdeux
                if Jun > Jdeux :
                    # alors assigne a la variable ligneDeux[2] est ??gal a "x"
                    ligneDeux[2] ="x"
                # si la variable Jdeux est sup??rieur a la variable Jun
                elif Jdeux > Jun :
                    # alors assigne a la variable ligneDeux[2] est ??gal a "o"
                    ligneDeux[2] ="o"
            # sinon
            else:
                # alors affiche "erreur"
                print("erreur")
        # si la variable Reponse est ??gal a "c2" ou "C2" ou "2C"
        elif Reponse == "c2" or Reponse == "C2" or Reponse == "2C":
            # alors si la variable ligneDeux[3] n'est pas ??gal a rien
            if ligneDeux[3] != "":
                # alors ??xecute coupJoueur
                coupJoueur()
            # si la variable ligneDeux[3] est ??gal a rien
            elif ligneDeux[3] == "":
                # alors si la variable Jun est sup??rieur a la variable Jdeux
                if Jun > Jdeux :
                    # alors assigne a la variable ligneDeux[3] est ??gal a "x"
                    ligneDeux[3] ="x"
                # si la variable Jdeux est sup??rieur a la variable Jun
                elif Jdeux > Jun :
                    # alors assigne a la variable ligneDeux[3] est ??gal a "o"
                    ligneDeux[3] ="o"
            # sinon
            else:
                print("erreur")
        # si la variable Reponse est ??gal a "a3" ou "A3"
        elif Reponse == "a3" or Reponse == "A3" or Reponse =="3A":
            # alors si la variable ligneTrois[1] n'est pas ??gal ?? rien
            if ligneTrois[1] != "":
                # alors ??xecute coupJoueur
                coupJoueur()
            # si la variable ligneTrois[1] est ??gal rien
            elif ligneTrois[1] == "":
                # alors si la variable Jun est sup??rieur a la variable Jdeux
                if Jun > Jdeux :
                    # alors assigne a la variable ligneTrois[1] "x"
                    ligneTrois[1] ="x"
                # si la variable Jdeux est sup??rieur a la variable Jun
                elif Jdeux > Jun :
                    # alors assigne a la variable ligneTrois[1] "o"
                    ligneTrois[1] ="o"
            # sinon
            else:
                # affiche "erreur"
                print("erreur")
        # si la variable Reponse est ??gal a "b3" ou "B3" ou "3B"
        elif Reponse == "b3" or Reponse == "B3" or Reponse == "3B":
            # alors si la variable ligneTrois[2] n'est pas ??gal ?? rien
            if ligneTrois[2] != "":
                # alors ??xecute coupJoueur
                coupJoueur()
            # si la variable ligneTrois[2] est ??gal rien
            elif ligneTrois[2] == "":
                # alors si la variable Jun est sup??rieur a la variable Jdeux
                if Jun > Jdeux :
                    # alors assigne a la variable ligneTrois[2] "x"
                    ligneTrois[2] ="x"
                # si la variable Jdeux est sup??rieur a la variable Jun
                elif Jdeux > Jun :
                    # alors assigne a la variable ligneTrois[2] "o"
                    ligneTrois[2] ="o"
            # sinon
            else:
                # affiche "erreur"
                print("erreur")
        # si la variable Reponse est ??gal a "c3" ou "C3" ou "3C"
        elif Reponse == "c3" or Reponse == "C3" or Reponse == "3C":
            # alors si la variable ligneTrois[3] n'est pas ??gal ?? rien
            if ligneTrois[3] != "":
                # alors ??xecute coupJoueur
                coupJoueur()
            # si la variable ligneTrois[3] est ??gal rien
            elif ligneTrois[3] == "":
                # alors si la variable Jun est sup??rieur a la variable Jdeux
                if Jun > Jdeux :
                    # alors assigne a la variable ligneTrois[3] "x"
                    ligneTrois[3] ="x"
                # si la variable Jdeux est sup??rieur a la variable Jun
                elif Jdeux > Jun :
                    # alors assigne a la variable ligneTrois[3] "o"
                    ligneTrois[3] ="o"
            # sinon
            else:
                # affiche "erreur"
                print("erreur")
# initialiser la variable afm a 0
afm = 0
# d??finir la fonction Bot
def Bot():
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
    # globaliser la variable Tableau
    global Tableau
    # globaliser la variable compteTour
    global compteTour
    # globaliser la variable afm
    global afm
    # assigne a la variable TableauRobot la liste [ligneUn[1],ligneUn[2],ligneUn[3],ligneDeux[1],ligneDeux[2],ligneDeux[3],ligneTrois[1],ligneTrois[2],ligneTrois[3]]
    TableauRobot = [ligneUn[1],ligneUn[2],ligneUn[3],ligneDeux[1],ligneDeux[2],ligneDeux[3],ligneTrois[1],ligneTrois[2],ligneTrois[3]]
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
    # si la variable afm est ??gal 0
    if afm == 0:
        # si la variable ligneUn[1] est ??gal a 'x' ou, la variable ligneUn[3] est ??gal a 'x' ou la variable ligneTrois[1] est ??gal a 'x' ou la variable ligneTrois[3] est ??gal a 'x'
        if ligneUn[1] == 'x' or ligneUn[3] == 'x' or ligneTrois[1] == 'x' or ligneTrois[3] == 'x':
            # alors assigne a la variable ligneDeux[2] 'o'
            ligneDeux[2] = 'o'
            # assigne a la varibale afm = 1
            afm = 1
            # retourne la fonction
            return
        # si la variable ligneDeux[2] est ??gal a 'x'
        if ligneDeux[2] == 'x':
            # alors assigne a la variable ligneUn[1] 'o'
            ligneUn[1] = 'o'
            # assigne a la variable afm 1
            afm = 1
            # retourne la fonction 
            return
        # si la variable ligneUn[2] est ??gal a 'x'
        if ligneUn[2] == 'x':
            # alors assigne a la variable ligneDeux[2] 'o'
            ligneDeux[2] = 'o'
            # assigne la variable afm 1
            afm = 1
            # retourne la fonction
            return
        # si la variable ligneDeux[1] est ??gal a 'x'
        if ligneDeux[1] == 'x':
            # alors assigne a la variable ligneDeux[2] 'o'
            ligneDeux[2] = 'o'
            # assigne la variable afm 1
            afm = 1
            # retourne la fonction
            return
        # si la variable ligneTrois[2] est ??gal a 'x'
        if ligneTrois[2] == 'x':
            # alors assigne a la variable ligneDeux[2] 'o'
            ligneDeux[2] = 'o'
            # assigne la variable afm 1
            afm = 1
            # retourne la fonction
            return
        # si la variable ligneDeux[3] est ??gal a 'x'
        if ligneDeux[3] == 'x':
            # alors assigne a la variable ligneDeux[2] 'o'
            ligneDeux[2] = 'o'
            # assigne la variable afm 1
            afm = 1
            # retourne la fonction
            return
    # si la variable afm est ??gal a 1
    if afm == 1:
        # pour la variable i dans la variable TableauRobot
        for i in TableauRobot:
            # si la variable i est ??gal a rien
            if i == "":
                # alors si la variable ligneUn.count('o') est ??gal a 2
                if ligneUn.count('o') == 2:
                    # alors alors pour i dans l'intervale (1, len(ligneUn))
                    for i in range(1, len(ligneUn)):
                        # si la variable ligneUn[i] est ??gal a rien
                        if ligneUn[i] == '':
                            # alors assigne a la variable ligneUn[i] 'o'
                            ligneUn[i] = 'o'
                            # retourner la fonction
                            return
                # si la variable ligneDeux.count('o') est ??gal a 2
                if ligneDeux.count('o') == 2:
                    # alors pour i dans l'intervale (1, len(ligneDeux))
                    for i in range(1, len(ligneDeux)):
                        # si la variable ligneDeux[i] est ??gal a rien
                        if ligneDeux[i] == '':
                            # alors assigne a la variable ligneDeux[i] 'o'
                            ligneDeux[i] = 'o'
                            # retourner la fonction
                            return
                # si la variable ligneTrois.count('o') est ??gal a 2
                if ligneTrois.count('o') == 2:
                    # alors pour i dans l'intervale (1, len(ligneTrois))
                    for i in range(1, len(ligneTrois)):
                        # si la variable ligneTrois[i] est ??gal a rien
                        if ligneTrois[i] == '':
                            # alors assigne a la variable ligneTrois[i] 'o'
                            ligneTrois[i] = 'o'
                            # retourner la fonction
                            return
                # si la variable colonneUn.count('o') est ??gal a 2
                if colonneUn.count('o') == 2:
                    # alors alors pour i dans l'ensemble (len(colonneUn))
                    for i in range(len(colonneUn)):
                        # si la variable colonneUn[i] est ??gal a rien
                        if colonneUn[i] == '':
                            # alors assigne a la variable colonneUn[i] 'o'
                            colonneUn[i] = 'o'
                            # assigne a la variable ligneUn[1] colonneUn[0]; a la variable ligneDeux[1] colonneUn[1]; a la variable ligneTrois[1] colonneUn[2]
                            ligneUn[1] = colonneUn[0];ligneDeux[1] = colonneUn[1];ligneTrois[1] = colonneUn[2]
                            # retourner la fonction
                            return
                # si la variable colonneDeux.count('o') est ??gal a 2
                if colonneDeux.count('o') == 2:
                    # alors pour i dans l'ensemble (len(colonneDeux))
                    for i in range(len(colonneDeux)):
                        # si la variable colonneDeux[i] est ??gal a rien
                        if colonneDeux[i] == '':
                            # alors assigne a la variable colonneDeux[i] 'o'
                            colonneDeux[i] = 'o'
                            # assigne a la variable ligneUn[2] colonneDeux[0]; a la variable ligneDeux[2] colonneDeux[1]; a la variable ligneTrois[2] colonneUn[2]
                            ligneUn[2] = colonneDeux[0];ligneDeux[2] = colonneDeux[1];ligneTrois[2] = colonneDeux[2]
                            # retourner la fonction
                            return
                # si la variable colonneTrois.count('o') est ??gal a 2
                if colonneTrois.count('o') == 2:
                    # alors pour i dans l'ensemble (len(colonneTrois))
                    for i in range(len(colonneTrois)):
                        # si la variable colonneTrois[i] est ??gal a rien
                        if colonneTrois[i] == '':
                            # alors assigne a la variable colonneTrois[i] 'o'
                            colonneTrois[i] = 'o'
                            # assigne a la variable ligneUn[3] colonneTrois[0]; a la variable ligneDeux[3] colonneTrois[1]; a la variable ligneTrois[3] colonneTrois[2]
                            ligneUn[3] = colonneTrois[0];ligneDeux[3] = colonneTrois[1];ligneTrois[3] = colonneTrois[2]
                            # retourner la fonction
                            return
                # si la variable diagoUn.count('o') est ??gal a 2
                if diagoUn.count('o') == 2:
                    # alors pour i dans l'ensemble (len(diagoUn))
                    for i in range(len(diagoUn)):
                        # si la variable diagoUn[i] est ??gal a rien
                        if diagoUn[i] == '':
                            # alors assigne a la variable diagoUn[i] 'o'
                            diagoUn[i] = 'o'
                            # assigne a la variable ligneUn[1] diagoUn[0]; a la variable ligneDeux[2] diagoUn[1]; a la variable ligneTrois[3] diagoUn[2]
                            ligneUn[1] = diagoUn[0];ligneDeux[2] = diagoUn[1];ligneTrois[3] = diagoUn[2]
                            # retourner la fonction
                            return
                # si la variable diagoDeux.count('o') est ??gal a 2
                if diagoDeux.count('o') == 2:
                    # alors pour i dans l'ensemble (len(diagoDeux))
                    for i in range(len(diagoDeux)):
                        # si la variable diagoDeux[i] est ??gal a rien
                        if diagoDeux[i] == '':
                            # alors assigne a la variable diagoDeux[i] 'o'
                            diagoDeux[i] = 'o'
                            # assigne a la variable ligneUn[3] diagoDeux[0]; a la variable ligneDeux[2] diagoDeux[1]; a la variable ligneTrois[1] diagoDeux[0]
                            ligneUn[3] = diagoDeux[2];ligneDeux[2] = diagoDeux[1];ligneTrois[1] = diagoDeux[0]
                            # retourner la fonction
                            return 
                # si la variable ligneUn.count('') est sup??rieur ou ??gal a 1
                if ligneUn.count('')>= 1:
                    # alors si la variable ligneUn.count('x') est ??gal a 2
                    if ligneUn.count('x') == 2:
                        # alors alors pour i dans l'intervale (1, len(ligneUn))
                        for i in range(1, len(ligneUn)):
                            # si la variable ligneUn[i] est ??gal a rien
                            if ligneUn[i] == '':
                                # alors assigne a la variable ligneUn[i] 'o'
                                ligneUn[i] = 'o'
                                # retourner la fonction
                                return
                # si la variable ligneDeux.count('') est sup??rieur ou ??gal a 1
                if ligneDeux.count('')>= 1:   
                    # alors si la variable ligneDeux.count('x') est ??gal a 2             
                    if ligneDeux.count('x') == 2:
                        # alors pour i dans l'intervale (1, len(ligneDeux))
                        for i in range(1, len(ligneDeux)):
                            # si la variable ligneDeux[i] est ??gal a rien
                            if ligneDeux[i] == '':
                                # alors assigne a la variable ligneDeux[i] 'o'
                                ligneDeux[i] = 'o'
                                # retourner la fonction
                                return
                # si la variable ligneTrois.count('') est sup??rieur ou ??gal a 1
                if ligneTrois.count('')>= 1:
                    # alors si la variable ligneTrois.count('x') est ??gal a 2
                    if ligneTrois.count('x') == 2:
                        # alors pour i dans l'intervale (1, len(ligneTrois))
                        for i in range(1, len(ligneTrois)):
                            # si la variable ligneTrois[i] est ??gal a rien
                            if ligneTrois[i] == '':
                                # alors assigne a la variable ligneTrois[i] 'o'
                                ligneTrois[i] = 'o'
                                # retourner la fonction
                                return
                # si la variable colonneUn.count('') est sup??rieur ou ??gal a 1
                if colonneUn.count('')>= 1:
                    # alors si la variable colonneUn.count('x') est ??gal a 2
                    if colonneUn.count('x') == 2:
                        # alors alors pour i dans l'ensemble (len(colonneUn))
                        for i in range(len(colonneUn)):
                            # si la variable colonneUn[i] est ??gal a rien
                            if colonneUn[i] == '':
                                # alors assigne a la variable colonneUn[i] 'o'
                                colonneUn[i] = 'o'
                                # assigne a la variable ligneUn[1] colonneUn[0]; a la variable ligneDeux[1] colonneUn[1]; a la variable ligneTrois[1] colonneUn[2]
                                ligneUn[1] = colonneUn[0];ligneDeux[1] = colonneUn[1];ligneTrois[1] = colonneUn[2]
                                # retourner la fonction
                                return
                # si la variable colonneDeux.count('') est sup??rieur ou ??gal a 1
                if colonneDeux.count('')>= 1:
                    # alors si la variable colonneDeux.count('x') est ??gal a 2             
                    if colonneDeux.count('x') == 2:
                        # alors pour i dans l'ensemble (len(colonneDeux))
                        for i in range(len(colonneDeux)):
                            # si la variable colonneDeux[i] est ??gal a rien
                            if colonneDeux[i] == '':
                                # alors assigne a la variable colonneDeux[i] 'o'
                                colonneDeux[i] = 'o'
                                # assigne a la variable ligneUn[2] colonneDeux[0]; a la variable ligneDeux[2] colonneDeux[1]; a la variable ligneTrois[2] colonneDeux[2]
                                ligneUn[2] = colonneDeux[0];ligneDeux[2] = colonneDeux[1];ligneTrois[2] = colonneDeux[2]
                                # retourner la fonction
                                return
                # si la variable colonneTrois.count('') est sup??rieur ou ??gal a 1
                if colonneTrois.count('')>= 1:
                    # alors si la variable colonneTrois.count('x') est ??gal a 2
                    if colonneTrois.count('x') == 2:
                        # alors pour i dans l'ensemble (len(colonneTrois))
                        for i in range(len(colonneTrois)):
                            # si la variable colonneTrois[i] est ??gal a rien
                            if colonneTrois[i] == '':
                                # alors assigne a la variable colonneTrois[i] 'o'
                                colonneTrois[i] = 'o'
                                # assigne a la variable ligneUn[3] colonneTrois[0]; a la variable ligneDeux[3] colonneTrois[1]; a la variable ligneTrois[3] colonneTrois[2]
                                ligneUn[3] = colonneTrois[0];ligneDeux[3] = colonneTrois[1];ligneTrois[3] = colonneTrois[2]
                                # retourner la fonction
                                return
                # si la variable diagoUn.count('') est sup??rieur ou ??gal a 1
                if diagoUn.count('')>= 1:
                    # alors si la variable diagoUn.count('x') est ??gal a 2        
                    if diagoUn.count('x') == 2:
                        # alors pour i dans l'ensemble (len(diagoUn))
                        for i in range(len(diagoUn)):
                            # si la variable diagoUn[i] est ??gal a rien
                            if diagoUn[i] == '':
                                # alors assigne a la variable diagoUn[i] 'o'
                                diagoUn[i] = 'o'
                                # assigne a la variable ligneUn[1] diagoUn[0]; a la variable ligneDeux[2] diagoUn[1]; a la variable ligneTrois[3] diagoUn[2]
                                ligneUn[1] = diagoUn[0];ligneDeux[2] = diagoUn[1];ligneTrois[3] = diagoUn[2]
                                # retourner la fonction
                                return
                # si la variable diagoDeux.count('') est sup??rieur ou ??gal a 1
                if diagoDeux.count('')>= 1:
                    # alors si la variable diagoDeux.count('x') est ??gal a 2
                    if diagoDeux.count('x') == 2:
                        # alors pour i dans l'ensemble (len(diagoDeux))
                        for i in range(len(diagoDeux)):
                            # si la variable diagoDeux[i] est ??gal a rien
                            if diagoDeux[i] == '':
                                # alors assigne a la variable diagoDeux[i] 'o'
                                diagoDeux[i] = 'o'
                                # assigne a la variable ligneUn[3] diagoDeux[2]; a la variable ligneDeux[2] diagoDeux[1]; a la variable ligneTrois[1] diagoDeux[0]
                                ligneUn[3] = diagoDeux[2];ligneDeux[2] = diagoDeux[1];ligneTrois[1] = diagoDeux[0]
                                # retourner la fonction
                                return
                # si la variable ligneUn[1] et ligneTrois[3] est ??gal a 'x'
                if ligneUn[1] == 'x' and ligneTrois[3] == 'x':
                    # alors si la variable ligneUn[2] est ??gal a rien
                    if ligneUn[2] == '':
                        # alors assigne a la variable ligneUn[2] 'o'
                        ligneUn[2] = 'o'
                        # retourner la fonction
                        return
                # si la variable ligneUn[3] et ligneTrois[1] est ??gal a 'x'
                if ligneUn[3] == 'x' and ligneTrois[1] == 'x':
                    # alors si la variable ligneUn[2] est ??gal a rien
                    if ligneUn[2] == '':
                        # alors assigne a la variable ligneUn[2] 'o'
                        ligneUn[2] = 'o'
                        # retourner la fonction
                        return
                # si la variable ligneDeux[2] et ligneTrois[3] est ??gal a 'x'
                if ligneDeux[2] == 'x' and ligneTrois[3] == 'x':
                    # alors si la variable ligneTrois[1] est ??gal a rien
                    if ligneTrois[1] == '':
                        # alors assigne a la variable ligneTrois[1] 'o'
                        ligneTrois[1] = 'o'
                        # retourner la fonction
                        return
                # si la variable ligneDeux[2] et ligneTrois[1] est ??gal a 'x'
                if ligneDeux[2] == 'x' and ligneTrois[1] == 'x':
                    # alors si la variable ligneUn[3] est ??gal a rien
                    if ligneUn[3] == '':
                        # alors assigne a la variable ligneUn[3] 'o'
                        ligneUn[3] = 'o'
                        # retourner la fonction
                        return
                # si la variable ligneDeux[2] et ligneUn[3] est ??gal a 'x'
                if ligneDeux[2] == 'x' and ligneUn[3] == 'x':
                    # alors si la variable ligneTrois[1] est ??gal a rien
                    if ligneTrois[1] == '':
                        # alors assigne a la variable ligneTrois[1] 'o'
                        ligneTrois[1] = 'o'
                        # retourner la fonction
                        return
                # si la variable ligneTrois[1] et ligneDeux[2] est ??gal a 'x'
                if ligneTrois[1] == 'x' and ligneDeux[2] == 'x':
                    # alors si la variable ligneUn[3] est ??gal a rien
                    if ligneUn[3] == '':
                        # alors assigne a la variable ligneTrois[3] 'o'
                        ligneDeux[3] = 'o'
                        # retourner la fonction
                        return
                # si la variable ligneTrois[2] est ??gal a 'x'
                if ligneTrois[2] == 'x':
                    # alors si la variable ligneUn[3] ou la variable ligneUn[1] est ??gal a x
                    if ligneUn[3] or ligneUn[1] == 'x':
                        # alors si la variable ligneTrois[3] est ??gal a rien
                        if ligneTrois[3] == '':
                            # alors assigne a la variable ligneTrois[3] 'o'
                            ligneTrois[3] = 'o'
                            # retourner la fonction
                            return
                # si la variable ligneUn[2] est ??gal a 'x'
                if ligneUn[2] == 'x':
                    # alors si la variable ligneUn[3] ou la variable ligneUn[1] est ??gal a x
                    if ligneUn[3] or ligneUn[1] == 'x':
                        # alors si la variable ligneUn[3] est ??gal a rien
                        if ligneUn[3] == '':
                            # alors assigne a la variable ligneDeux[3] 'o'
                            ligneDeux[3] = 'o'
                            # retourner la fonction
                            return         
                # si la variable diagoUn.count('o') est ??gal a 1
                if diagoUn.count('o') == 1:
                    # alors alors pour la variable i dans la range(len(diagoUn))
                    for i in range(len(diagoUn)):
                        # si la variable diagoUn[i] est ??gal a rien
                        if diagoUn[i] == '':
                            # alors assigne a la variable diagoUn[i] 'o'
                            diagoUn[i] = 'o'
                            # assigne a la variable ligneUn[1] diagoUn[0]; a la variable ligneDeux[2] diagoUn[1]; a la variable ligneTrois[3] diagoUn[2]
                            ligneUn[1] = diagoUn[0];ligneDeux[2] = diagoUn[1];ligneTrois[3] = diagoUn[2]
                            # retourner la fonction
                            return
                # si la variable diagoDeux.count('o') est ??gal a 1
                if diagoDeux.count('o') == 1:
                    # alors pour la variable i dans la range(len(diagoDeux))
                    for i in range(len(diagoDeux)):
                        # si la variable diagoDeux[i] est ??gal a rien
                        if diagoDeux[i] == '':
                            # alors assigne a la variable diagoDeux[i] 'o'
                            diagoDeux[i] = 'o'
                            # assigne a la variable ligneUn[3] diagoDeux[2]; a la variable ligneDeux[2] diagoDeux[1]; a la variable ligneTrois[1] diagoDeux[0]
                            ligneUn[3] = diagoDeux[2];ligneDeux[2] = diagoDeux[1];ligneTrois[1] = diagoDeux[0]
                            # retourner la fonction
                            return
                # si la variable ligneUn.count('o') est ??gal a 1         
                if ligneUn.count('o') == 1:
                    # alors pour la variable i dans la range(len(ligneUn))
                    for i in range(1, len(ligneUn)):
                        # si la variable ligneUn[i] est ??gal a rien
                        if ligneUn[i] == '':
                            # alors assigne a la variable ligneUn[i] 'o'
                            ligneUn[i] = 'o'
                            # retourner la fonction
                            return
                # si la variable ligneDeux.count('o') est ??gal a 1
                if ligneDeux.count('o') == 1:
                    # alors pour la variable i dans la range(len(ligneDeux))
                    for i in range(1, len(ligneDeux)):
                        # si la variable ligneDeux[i] est ??gal a rien
                        if ligneDeux[i] == '':
                            # alors assigne a la variable ligneDeux[i] 'o'
                            ligneDeux[i] = 'o'
                            # retourner la fonction
                            return
                # si la variable ligneTrois.count('o') est ??gal a 1
                if ligneTrois.count('o') == 1:
                    # alors pour la variable i dans la range(len(ligneTrois))
                    for i in range(1, len(ligneTrois)):
                        # si la variable ligneTrois[i] est ??gal a rien
                        if ligneTrois[i] == '':
                            # alors assigne a la variable ligneTrois[i] 'o'
                            ligneTrois[i] = 'o'
                            # retourner la fonction
                            return
                # si la variable colonneUn.count('o') est ??gal a 1
                if colonneUn.count('o') == 1:
                    # alors pour la variable i dans la range(len(colonneUn))
                    for i in range(len(colonneUn)):
                        # si la variable colonneUn[i] est ??gal a rien
                        if colonneUn[i] == '':
                            # alors assigne a la variable colonneUn[i] 'o'
                            colonneUn[i] = 'o'
                            # assigne a la variable ligneUn[1] colonneUn[0]; a la variable ligneDeux[1] colonneUn[1]; a la variable ligneTrois[1] colonneUn[2]
                            ligneUn[1] = colonneUn[0];ligneDeux[1] = colonneUn[1];ligneTrois[1] = colonneUn[2]
                            # retourner la fonction
                            return
                # si la variable colonneDeux.count('o') est ??gal a 1
                if colonneDeux.count('o') == 1:
                    # alors pour la variable i dans la range(len(colonneDeux))
                    for i in range(len(colonneDeux)):
                        # si la variable colonneDeux[i] est ??gal a rien
                        if colonneDeux[i] == '':
                            # alors assigne a la variable colonneDeux[i] 'o'
                            colonneDeux[i] = 'o'
                            # assigne a la variable ligneUn[2] colonneDeux[0]; a la variable ligneDeux[2] colonneDeux[1]; a la variable ligneTrois[2] colonneDeux[2]
                            ligneUn[2] = colonneDeux[0];ligneDeux[2] = colonneDeux[1];ligneTrois[2] = colonneDeux[2]
                            # retourner la fonction
                            return
                # si la variable colonneTrois.count('o') est ??gal a 1
                if colonneTrois.count('o') == 1:
                    # alors pour la variable i dans la range(len(colonneTrois))
                    for i in range(len(colonneTrois)):
                        # si la variable colonneTrois[i] est ??gal a rien
                        if colonneTrois[i] == '':
                            # alors assigne a la variable colonneTrois[i] 'o'
                            colonneTrois[i] = 'o'
                            # assigne a la variable ligneUn[3] colonneTrois[0]; a la variable ligneDeux[3] colonnetrois[1]; a la variable ligneTrois[3] colonneTrois[2]
                            ligneUn[3] = colonneTrois[0];ligneDeux[3] = colonneTrois[1];ligneTrois[3] = colonneTrois[2]
                            # retourner la fonction
                            return

# initialiser la variable explication a 0
explication = 0
# d??finir la fonction StarterGame
def StarterGame():
    # globaliser la variable explication
    global explication
    # si la variable explication est ??gal a 0
    if explication == 0:
        # alors afficher "yo sale dino, je t'explique les r??gle ^^, :"
        print("yo sale dino, je t'explique les r??gle ^^, :")
        # afficher "le morpion, le joueur 1 c'est la croix, joueur 2 le rond, celui qui arrive a alligner dans le cube de 3 sur 3, 3 X ou 3 O a gagner"
        print("le morpion, le joueur 1 c'est la croix, joueur 2 le rond, celui qui arrive a alligner dans le cube de 3 sur 3, 3 X ou 3 O a gagner")
        # afficher "voila bon bonne chance !"
        print("voila bon bonne chance !")
        # assigner a la variable explication 1
        explication = 1
    
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
    # initialise la variable gagnant 3
    gagnant = 3
    # afficher "me revoila tu veux te taper contre qui ? le bot ou un pote ?"
    print("me revoila tu veux te taper contre qui ? le bot ou un pote ?")
    # afficher "r??ponse possible : "
    print("r??ponse possible : ")
    # afficher "-bot" et "-pote"
    print("-bot");print("-pote")
    # assigne a la variable demande "Restart"
    demande = "Restart"
    # assigne a la variable demande, le retour de l'execution de la fonction input de param??tre "votre choix: "
    demande = input("votre choix: ")
    # si la variable demande n'est pas dans la liste ["bot","pote"]
    if not demande in["bot","pote"]:
        # alors afficher "tu me mes roublise, stp mes une valeur possible pas :",demande
        print("tu me mes roublise, stp mes une valeur possible pas :",demande)
        # ??xecuter la fonction StarterGame
        StarterGame()
    # si la variable demande est dans la liste ["bot","pote"]
    if demande in ["bot","pote"]:
        # alors si la variable demande est ??gal a "pote"
        if demande == "pote":
            # afficher Tableau
            print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
            # tant que la variable gagnant n'est pas dans la liste [0,1,2]
            while not gagnant in [0,1,2]:
                # si la variable gagnant n'est pas dans la liste [0,1,2]
                if not gagnant in [0,1,2]:
                    # alors assigne a la variable Jun, la variable Jdeux + 1
                    Jun = Jdeux + 1
                    # ??xecute coupJoueur
                    coupJoueur()
                    # assigne a la variable compteTour, la variable compteTour + 1
                    compteTour = compteTour + 1
                    # affiche Tableau
                    print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
                    # ??xecute winner
                    winner()
                # si la variable gagnant n'est pas dans la liste [0,1,2]
                if not gagnant in [0,1,2]:  
                    # alors assigne a la variable Jdeux, la variable Jun + 1 
                    Jdeux = Jun + 1
                    # ??xecute coupJoueur
                    coupJoueur()
                    # assigne a la variable compteTour, la variable compteTour + 1
                    compteTour = compteTour + 1
                    # affiche Tableau
                    print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
                    # ??xecute winner
                    winner()
            # Si la variable gagnant est ??gal a 0
            if gagnant == 0:
                # alors affiche "matche nul, vous ??tes nul !"
                print("matche nul, vous ??tes nul !")
                # ??xecute la fonction Restart    
                Restart()
            # si la variable gagnant est ??gal 1
            elif gagnant == 1:
                # alors affiche "joueur 1 (ps celui qui a les x ) est gagnant, ps le joueur 2 tes nul"
                print("joueur 1 (ps celui qui a les x ) est gagnant, ps le joueur 2 tes nul")
                # ??xecute la fonction Restart
                Restart()
            # si la variable gagnant est ??gal 2
            elif gagnant == 2:
                # alors affiche "joueur 2 (ps celui qui a les o ) est gagnant, ps le joueur 1 tes nul"
                print("le joueur 2 (ps celui qui a les o ) est gagnant, ps le joueur 1 tes nul")
                # ??xecute la fonction Restart
                Restart()
        # si la variable demande est ??gal a "bot"
        if demande == "bot":
            # afficher Tableau
            print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
            # tant que la variable gagnant n'est pas dans la liste [0,1,2]
            while not gagnant in [0,1,2]:
                # si la variable gagnant n'est pas dans la liste [0,1,2]
                if not gagnant in [0,1,2]:
                    # alors assigne a la variable Jun, la variable Jdeux + 1
                    Jun = Jdeux + 1
                    # ??xecute coupJoueur
                    coupJoueur()
                    # assigne a la variable compteTour, la variable compteTour + 1
                    compteTour = compteTour + 1
                    # affiche Tableau
                    print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
                    # ??xecute winner
                    winner()
                # si la variable gagnant n'est pas dans la liste [0,1,2]
                if not gagnant in [0,1,2]:  
                    # alors assigne a la variable Jdeux, la variable Jun + 1 
                    Jdeux = Jun + 1
                    # ??xecute coupJoueur
                    coupJoueur()
                    # assigne a la variable compteTour, la variable compteTour + 1
                    compteTour = compteTour + 1
                    # affiche Tableau
                    print(Tableau[0]);print(Tableau[1]);print(Tableau[2]);print(Tableau[3])
                    # ??xecute winner
                    winner()
            # Si la variable gagnant est ??gal a 0
            if gagnant == 0:
                # alors affiche "matche nul, vous ??tes nul !"
                print("matche nul, vous ??tes nul !")
                # ??xecute la fonction Restart    
                Restart()
            # si la variable gagnant est ??gal 1
            elif gagnant == 1:
                # alors affiche "joueur 1 (ps celui qui a les x ) est gagnant, ps le joueur 2 tes nul"
                print("joueur 1 (ps celui qui a les x ) est gagnant, ps le joueur 2 tes nul")
                # ??xecute la fonction Restart
                Restart()
            # si la variable gagnant est ??gal 2
            elif gagnant == 2:
                # alors affiche "joueur 2 (ps celui qui a les o ) est gagnant, ps le joueur 1 tes nul"
                print("le joueur 2 (ps celui qui a les o ) est gagnant, ps le joueur 1 tes nul")
                # ??xecute la fonction Restart
                Restart()
# ??xecute la fonction StarterGame
StarterGame()