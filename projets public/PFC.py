# Debut

# on admet la fonction random qui génère un nombre entre 0 et 2 
# on admet la fonction input qui récup les entrés du jouer 

# définir une fonction règles avec comme pramètre rules
    # attendre 1 secondes
    # afficher "Bienvenue dans ce magnifique shifumi"
    # attendre 1 secondes
    # afficher "les règles sont simples"
    # attendre 1 secondes
    # afficher "vous allez devoir choisir si voulez jouer contre un autre joueur ou contre un bot"
    # attendre 1 secondes
    # afficher "ensuite chaque joueur devras choisir pierre, papier ou ciseaux"
    # attendre 1 secondes
    # afficher "la pierre casse les ciseaux, la papier cache la pierre et les ciseaux coupe le papier" 


# definir une fonction modeDeJeux avec comme paramètre joueur et bot
    # afficher via le retour de l'execution de la fonction print de paramètre "souhaitez vous jouer contre un joueur ou contre un bot"
    # assigner a la variable joueurOuBot le retour de l'execution de la fonction input 
    # si joueurOuBot est égal a joueur 
         # alors éxecute la fonction joueurContreJoueur
    # si joueurOuBot est égal a bot
        # alors éxecute la fonction joueurContreBot
    # sinon retourner la fonction modeDeJeux

# éxécuter la fonction modeDeJeux

# definir une fonction joueurContreJoueur de paramètre pierre, papier ou ciseaux    
    #assigner a la variable player1 le retour de l'execution de la fonction input de paramètre "Pierre, papier ou ciseaux "
    #assigner a la variable player2 le retour de l'execution de la fonction input de paramètre "Pierre, papier ou ciseaux "
    # initialiser la variable pointPlayer1 a 0
    # initialiser la variable pointPlayer2 a 0
    #tant que pointPlayer1 ou pointPlayer2 n'est pas égal 3 
        # si player1 est égal a pierre
            # si player2 est égal a pierre
                # alors afficher "égalité"
            # si player2 est égal a papier
                # alors afficher "Le joueur 2 a gagner ce round"
            # assigner a la variable pointPlayer2, pointPlayer2 + 1 
            # si player2 est égal a ciseaux                # alors afficher "Le joueur 1 a gagner ce round"
            # assigner a la variable pointPlayer1, pointPlayer1 + 1 
        # si player1 est égal a papier
            # si player2 est égal a pierre
                # alors afficher "Le joueur 1 a gagner ce round"
            # assigner a la variable pointPlayer1, pointPlayer1 + 1 
            # si player2 est égal a papier
                # alors afficher "égalité"
            # si player2 est égal a ciseaux                # alors afficher "Le joueur 2 a gagner ce round"
            # assigner a la variable pointPlayer2, pointPlayer2 + 1 
        # si player1 est égal a ciseaux            # si player2 est égal a pierre
                # alors afficher "Le joueur 2 a gagner ce round"
            # assigner a la variable pointPlayer2, pointPlayer2 + 1 
            # si player2 est égal a papier
                # alors afficher "Le joueur 1 a gagner ce round"
            # assigner a la variable pointPlayer1, pointPlayer1 + 1 
            # si player2 est égal a ciseaux                # alors afficher "égalité"
        # afficher pointPlayer1, '-', pointPlayer2
    # si pointPlayer1 égal a 3
        # alors afficher "le joueur 1 a gagné"
    # si pointPlayer2 égal a 3
        # alors afficher "le joueur 2 a gagné"
    #assigner a la variable restart le retour de l'execution de la fonction input de paramètre "Voulez vous recommencer: "
    # if restart égal a "oui"
        # alors retourner la fonction JoueurContreJoueur

# definir une fonction joueurContreBot de paramètre pierre, papier ou ciseaux 
    #assigner a la variable player1 le retour de l'execution de la fonction input de paramètre "Pierre, papier ou ciseaux "
    # assigner a la variable Bot le retour de l'execution de la fonction random
    # initialiser la variable pointPlayer1 a 0
    # initialiser la variable pointBot a 0
    #tant que pointPlayer1 ou pointBot n'est pas égal 3 
        # si player1 est égal a pierre
            # si Bot est égal a 0
                # alors afficher "égalité"
            # si Bot est égal a 1
                # alors afficher "Le Bot a gagner ce round"
            # assigner a la variable pointBot, pointBot + 1 
            # si Bot est égal a 2
                # alors afficher "Le joueur 1 a gagner ce round"
            # assigner a la variable pointPlayer1, pointPlayer1 + 1 
        # si player1 est égal a papier
            # si Bot est égal a 0
                # alors afficher "Le joueur 1 a gagner ce round"
            # assigner a la variable pointPlayer1, pointPlayer1 + 1 
            # si Bot est égal a 1
                # alors afficher "égalité"
            # si Bot est égal a 2
                # alors afficher "Le Bot a gagner ce round"
            # assigner a la variable pointBot, pointBot + 1 
        # si player1 est égal a ciseaux            # si Bot est égal a 0
                # alors afficher "Le Bot a gagner ce round"
            # assigner a la variable pointBot, pointBot + 1 
            # si Bot est égal a 1
                # alors afficher "Le joueur 1 a gagner ce round"
            # assigner a la variable pointPlayer1, pointPlayer1 + 1 
            # si Bot est égal a 2
                # alors afficher "égalité"
        # afficher pointPlayer1, '-', pointBot
    # si pointPlayer1 égal a 3
        # alors afficher "le joueur 1 a gagné"
    # si pointBot égal a 3
        # alors afficher "le Bot a gagné"
    #assigner a la variable restart le retour de l'execution de la fonction input de paramètre "Voulez vous recommencer: "
    # if restart égal a "oui"
        # alors retourner la fonction JoueurContreBot
      

#FIN