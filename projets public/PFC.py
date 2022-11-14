# Debut

# on admet la fonction time qui permet d'attendre entre entre 2 commande
import time
# on admet la fonction random qui génère un nombre entre 0 et 2 
import random
# on admet la fonction input qui récup les entrés du jouer 
# import input

# définir une fonction règles avec comme pramètre rules
def règles():
    # attendre 1 secondes
    time.sleep(1)
    # afficher "Bienvenue dans ce magnifique shifumi"
    print("Bienvenue dans ce magnifique shifumi")
    # attendre 1 secondes
    time.sleep(1)
    # afficher "les règles sont simples"
    print("les règles sont simples")
    # attendre 1 secondes
    time.sleep(1)
    # afficher "vous allez devoir choisir si voulez jouer contre un autre joueur ou contre un bot"
    print("vous allez devoir choisir si voulez jouer contre un autre joueur ou contre un bot")
    # attendre 1 secondes
    time.sleep(1)
    # afficher "ensuite chaque joueur devras choisir pierre, papier ou ciseaux"
    print("ensuite chaque joueur devras choisir pierre, papier ou ciseaux")
    # attendre 1 secondes
    time.sleep(1)
    # afficher "la pierre casse les ciseaux, la papier cache la pierre et les ciseaux coupe le papier" 
    print("la pierre casse les ciseaux, la papier cache la pierre et les ciseaux coupe le papier")
    # éxécuter la fonction modeDeJeux
    modeDeJeux()


# definir une fonction modeDeJeux avec comme paramètre
def modeDeJeux():
    # assigner a la variable joueurOuBot le retour de l'execution de la fonction input 
    joueurOuBot=input("souhaitez vous jouer contre un joueur ou contre un bot: ")
    # si joueurOuBot est égal a joueur
    if joueurOuBot == "joueur":
         # alors éxecute la fonction joueurContreJoueur
         joueurContreJoueur()
    # si joueurOuBot est égal a bot
    elif joueurOuBot == "bot":
        # alors éxecute la fonction joueurContreBot
        joueurContreBot()
    # sinon retourner la fonction modeDeJeux
    elif joueurOuBot != "joueur" or "bot":
        return modeDeJeux()


# definir une fonction joueurContreJoueur de paramètre   
def joueurContreJoueur():
    # initialiser la variable pointPlayer1 a 0
    pointPlayer1 = 0
    # initialiser la variable pointBot a 0
    pointPlayer2 = 0
    #tant que pointPlayer1 ou pointPlayer2 n'est pas égal 3
    while pointPlayer1 or pointPlayer2 != 3 :
        #assigner a la variable player1 le retour de l'execution de la fonction input de paramètre "Pierre, papier ou ciseaux "
        player1 = input("Pierre, papier ou ciseaux: ")
        #assigner a la variable player2 le retour de l'execution de la fonction input de paramètre "Pierre, papier ou ciseaux "
        player2 = input("Pierre, papier ou ciseaux: ")
        # si player1 est égal a pierre
        if player1 == "pierre":
            # si player2 est égal a pierre
            if player2 == "pierre":
                # alors afficher "égalité"
                print("égalité")
            # si player2 est égal a papier
            elif player2 == "papier":
                # alors afficher "Le joueur 2 a gagner ce round"
                print("Le joueur 2 a gagner ce round")
                # assigner a la variable pointPlayer2, pointPlayer2 + 1 
                pointPlayer2 = pointPlayer2 + 1
            # si player2 est égal a ciseaux  
            if player2 == "ciseaux":              
                # alors afficher "Le joueur 1 a gagner ce round"
                print("Le joueur 1 a gagner ce round")
                # assigner a la variable pointPlayer1, pointPlayer1 + 1 
                pointPlayer1 = pointPlayer1 + 1
        # si player1 est égal a papier
        elif player1 == "papier":
            # si player2 est égal a pierre
            if player2 == "pierre":
                # alors afficher "Le joueur 1 a gagner ce round"
                print("Le joueur 1 a gagner ce round")
                # assigner a la variable pointPlayer1, pointPlayer1 + 1 
                pointPlayer1 = pointPlayer1 + 1
            # si player2 est égal a papier
            elif player2 == "papier":
                # alors afficher "égalité"
                print("égaliter")
            # si player2 est égal a ciseaux
            elif player2 == "ciseaux":
                # alors afficher "Le joueur 2 a gagner ce round"
                print("Le joueur 2 a gagner ce round")
                # assigner a la variable pointPlayer2, pointPlayer2 + 1 
                pointPlayer2 = pointPlayer2 + 1 
        # si player1 est égal a ciseaux
        elif player1 == "ciseaux":
            # si player2 est égal a pierre
            if player2 == "pierre":
                # alors afficher "Le joueur 2 a gagner ce round"
                print("Le joueur 2 a gagner ce round")
                # assigner a la variable pointPlayer2, pointPlayer2 + 1 
                pointPlayer2 = pointPlayer2 + 1
            # si player2 est égal a papier
            elif player2 == "papier":
                # alors afficher "Le joueur 1 a gagner ce round"
                print("Le joueur 1 a gagner ce round")
                # assigner a la variable pointPlayer1, pointPlayer1 + 1
                pointPlayer1 = pointPlayer1 + 1
            # si player2 est égal a ciseaux
            elif player2 == "ciseaux":               
                # alors afficher "égalité"
                print("égaliter")
        # afficher pointPlayer1, '-', pointPlayer2
        print(pointPlayer1, "-", pointPlayer2)
    # si pointPlayer1 égal a 3
    if pointPlayer1 == 3:
        # alors afficher "le joueur 1 a gagné"
        print("Le joueur 1 a gagné")
    # si pointPlayer2 égal a 3
    elif pointPlayer2 == 3:
        # alors afficher "le joueur 2 a gagné"
        print("Le joueur 2 a gagné")
    #assigner a la variable restart le retour de l'execution de la fonction input de paramètre "Voulez vous recommencer: "
    restart = input("Voulez vous recommencer: ")
    # if restart égal a "oui"
    if restart == "oui":
        # alors retourner la fonction JoueurContreJoueur
        return joueurContreJoueur()

# definir une fonction joueurContreJoueur de paramètre   
def joueurContreBot():
    # initialiser la variable pointPlayer1 a 0
    pointPlayer = 0
    # initialiser la variable pointBot a 0
    pointBot = 0
    #tant que pointPlayer1 ou pointBot n'est pas égal 3
    while pointPlayer or pointBot != 3 :
        #assigner a la variable player1 le retour de l'execution de la fonction input de paramètre "Pierre, papier ou ciseaux "
        player = input("joueur, choisissez entre pierre, papier ou ciseaux: ")
        #assigner a la variable Bot le retour de l'execution de la fonction input de paramètre "Pierre, papier ou ciseaux "
        Bot = random.randint(0,2)
        # si player est égal a pierre
        if player == "pierre":
            # si Bot est égal a pierre
            if Bot == 0:
                # alors afficher "égalité"
                print("égalité")
            # si Bot est égal a papier
            elif Bot == 1:
                # alors afficher "Le bot a gagner ce round"
                print("Le bot a gagner ce round")
                # assigner a la variable pointBot, pointBot + 1 
                pointBot = pointBot + 1
            # si Bot est égal a ciseaux  
            if Bot == 2:              
                # alors afficher "Le joueur a gagner ce round"
                print("Le joueur a gagner ce round")
                # assigner a la variable pointPlayer, pointPlayer + 1 
                pointPlayer = pointPlayer + 1
        # si player est égal a papier
        elif player == "papier":
            # si Bot est égal a pierre
            if Bot == 0:
                # alors afficher "Le joueur a gagner ce round"
                print("Le joueur a gagner ce round")
                # assigner a la variable pointPlayer, pointPlayer + 1 
                pointPlayer = pointPlayer + 1
            # si Bot est égal a papier
            elif Bot == 1:
                # alors afficher "égalité"
                print("égaliter")
            # si Bot est égal a ciseaux
            elif Bot == 2:
                # alors afficher "Le bot a gagner ce round"
                print("Le bot a gagner ce round")
                # assigner a la variable pointBot, pointBot + 1 
                pointBot = pointBot + 1 
        # si player est égal a ciseaux
        elif player == "ciseaux":
            # si Bot est égal a pierre
            if Bot == 0:
                # alors afficher "Le bot a gagner ce round"
                print("Le bot a gagner ce round")
                # assigner a la variable pointBot, pointBot + 1 
                pointBot = pointBot + 1
            # si Bot est égal a papier
            elif Bot == 1:
                # alors afficher "Le joueur a gagner ce round"
                print("Le joueur a gagner ce round")
                # assigner a la variable pointPlayer, pointPlayer + 1
                pointPlayer = pointPlayer + 1
            # si Bot est égal a ciseaux
            elif Bot == 2:               
                # alors afficher "égalité"
                print("égaliter")
        # afficher pointPlayer, '-', pointBot
        print(pointPlayer, "-", pointBot)
    # si pointPlayer égal a 3
    if pointPlayer == 3:
        # alors afficher "le joueur a gagné"
        print("Le joueur a gagné")
    # si pointBot égal a 3
    elif pointBot == 3:
        # alors afficher "le bot a gagné"
        print("Le bot a gagné")
    #assigner a la variable restart le retour de l'execution de la fonction input de paramètre "Voulez vous recommencer: "
    restart = input("Voulez vous recommencer: ")
    # if restart égal a "oui"
    if restart == "oui":
        # alors retourner la fonction JoueurContreJoueur
        return joueurContreBot()


# éxécuter la fonction règles
règles()

#FIN