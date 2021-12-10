import random
from colorama import init
init()
from colorama import Back, Style

def posLettre(motSecret, devine, devineTab, positionLettre, numeroLettre):
    lettreEmplacement = -1;
    DejaPris = False;
    for i in range(6):
        #Est-ce que la lettre est présente dans le mot?
        if (devine == motSecret[i]):
            #Si oui, on vérifie sa position
            for j in range(6):
                #Est-ce que la lettre est déjà enregistrer?
                if (positionLettre[j] == i):
                    #on regarde les positions de lettre
                    for k in range(6):
                        if (positionLettre[k] == i):
                        #Est-ce qu'elle est à l'emplacement exacte?
                            if devineTab[k] != motSecret[k]:
                                #Non = on la reset
                                positionLettre[k] = -1;
                                lettreEmplacement = i;
                            else:
                                #oui = on la remet comme avant
                                positionLettre[k] = i;
                                if (k == numeroLettre):
                                    lettreEmplacement = i;
                    DejaPris = True;
            if (DejaPris == False):
                lettreEmplacement = i;
    #Mettre dans le bon ordre les lettres similaires
    for i in range(6):
        if (devine == devineTab[i]):
            if (i != numeroLettre):
                if (motSecret[numeroLettre] == motSecret[i]):
                    if (lettreEmplacement < positionLettre[i]):
                        nombreStock = positionLettre[i];
                        positionLettre[i] = lettreEmplacement;
                        lettreEmplacement = nombreStock;
    
    return lettreEmplacement;
        

positionLettre = [-1]*6;
#mot aléatoire de la liste
fichier = open("ListeMots.txt", "r");
listeLigne = fichier.readlines();
tailleLigne = len(listeLigne) - 1;
randomLigne = random.randint(0, tailleLigne);
motTest = listeLigne[randomLigne];
fichier.close();

motSecret = "";
#enlever le passage à la ligne de la chaine de caractères
for i in range(6):
    motSecret += motTest[i];

motSecret = "banane";
erreur = 0;
nombreTentatives = 8;
presenceCheck = False;

while erreur < nombreTentatives:
    devine = input("\n Quel mot de 6 lettres est le mot mystère? \n");
    #Mettre le mot à 6 lettres minimum
    while len(devine) < 6:
        devine += " ";
    #obtenir la position de chaque lettre
    for i in range(6):
        positionLettre[i] = posLettre(motSecret, devine[i], devine, positionLettre, i);
    print(positionLettre);
    #mettre la couleur en fonction de la correspondance
    for i in range(6):
        if (positionLettre[i] == -1):
            print(Back.BLUE, end = " ");
        else:
            if (positionLettre[i] == i):
                print(Back.RED, end=" ");
            else:
                print(Back.YELLOW, end = " ");
        
        print(devine[i], end=" ");
        print(Style.RESET_ALL, end = "");
    if (devine == motSecret):
        print("\n T'as gagné!");
        break;
    #nombre d'erreur
    erreur += 1;
    print("\n Plus que ", (nombreTentatives - erreur), " essaies");
if (erreur == nombreTentatives):
    print("\n Vous avez perdu, le mot était", motSecret);