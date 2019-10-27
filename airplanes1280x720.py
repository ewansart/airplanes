# Premier Projet d'Informatique

import pygame, math, random

# CONSTANTES

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (96, 96, 96)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
VERT_FONCE = (0, 155, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)
BLEU_CIEL = (119, 181, 254)
HERBE = (34, 120, 15)
MAUVE = (153, 0, 153)

DROITE = pygame.K_RIGHT
GAUCHE = pygame.K_LEFT
HAUT = pygame.K_UP
BAS = pygame.K_DOWN
D = pygame.K_d
Q = pygame.K_q
Z = pygame.K_z
S = pygame.K_s
MENU_DROITE = pygame.K_RIGHT
MENU_GAUCHE = pygame.K_LEFT
MENU_HAUT = pygame.K_UP
MENU_BAS = pygame.K_DOWN
ENTREE = pygame.K_RETURN
P = pygame.K_p
ESPACE = pygame.K_SPACE

PI = math.pi

# PARAMETRES

# Fenetre
FENETRE_LARGEUR = 1280
FENETRE_HAUTEUR = 720
IMAGES_PAR_SECONDE = 60

# Jeu
VIE_MAX = 10
TAILLE = 15
MANIABILITE = 25
VITESSE_MAX = 8
VITESSE_MIN = VITESSE_MAX//2
PUISSANCE = 20
RESISTANCE = 20
DELAI_TIR = 15
BALLE_VITESSE = 15
BALLE_LONGUEUR = 20
BALLE_EPAISSEUR = 3
MANCHE_MIN = 3
COLLISION = False
POWER = True
GRAVITE = 6

# FONCTIONS

def gerer_entree():
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            global Fini, Jeu
            Fini = True

        if(Jeu == False and evenement.type == pygame.KEYDOWN and evenement.key == ENTREE):
            Jeu = True

        else:
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == P or evenement.key == ESPACE:
                    global Pause, Pause_delai
                    Pause_delai = 100
                    if Pause:
                        Pause = False
                    else:
                        Pause = True
            if Pause:
                if evenement.type == pygame.KEYDOWN:
                    global select
                    if evenement.key == HAUT or evenement.key == Z:
                        select[0] -= 1
                    elif evenement.key == BAS or evenement.key == S:
                        select[0] += 1
                    elif evenement.key == ENTREE:
                        if select[0] == 0:
                            Pause = False
                        if select[0] == 1:
                            Pause = False
                            reinitialiser(True)
                            for avion in avions:
                                avion['score'] = 0
                                avion['ajoute_vitesse'] = 0
                                avion['ajoute_inclinaison'] = 0
                        if select[0] == 2:
                            Pause = False
                            reinitialiser(True)
                            Jeu = False


            else:
                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == DROITE:
                        avions[0]['ajoute_inclinaison'] += PI * (MANIABILITE/1000)
                    if evenement.key == GAUCHE:
                        avions[0]['ajoute_inclinaison'] -= PI * (MANIABILITE/1000)
                    if evenement.key == HAUT:
                        avions[0]['ajoute_vitesse'] += PUISSANCE/1000
                    if evenement.key == BAS:
                        avions[0]['ajoute_vitesse'] -= PUISSANCE/1000

                    if evenement.key == D:
                        avions[1]['ajoute_inclinaison'] += PI * (MANIABILITE/1000)
                    if evenement.key == Q:
                        avions[1]['ajoute_inclinaison'] -= PI * (MANIABILITE/1000)
                    if evenement.key == Z:
                        avions[1]['ajoute_vitesse'] += PUISSANCE/1000
                    if evenement.key == S:
                        avions[1]['ajoute_vitesse'] -= PUISSANCE/1000

                if evenement.type == pygame.KEYUP:

                    if evenement.key == DROITE:
                        avions[0]['ajoute_inclinaison'] -= PI * (MANIABILITE/1000)
                    if evenement.key == GAUCHE:
                        avions[0]['ajoute_inclinaison'] += PI * (MANIABILITE/1000)
                    if evenement.key == HAUT:
                        avions[0]['ajoute_vitesse'] -= PUISSANCE/1000
                    if evenement.key == BAS:
                        avions[0]['ajoute_vitesse'] += PUISSANCE/1000

                    if evenement.key == D:
                        avions[1]['ajoute_inclinaison'] -= PI * (MANIABILITE/1000)
                    if evenement.key == Q:
                        avions[1]['ajoute_inclinaison'] += PI * (MANIABILITE/1000)
                    if evenement.key == Z:
                        avions[1]['ajoute_vitesse'] -= PUISSANCE/1000
                    if evenement.key == S:
                        avions[1]['ajoute_vitesse'] += PUISSANCE/1000


def gerer_entree_menu():
    for evenement in pygame.event.get():
        global select, Fini, Jeu, Option
        if evenement.type == pygame.QUIT:
            Fini = True
        elif evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_BACKSPACE:
                if (select[1]+select[0]*12) < len(options) and options[select[1]] < 100 :
                    if select[1]+select[0]*12 == 10:
                        options[10] = False
                    elif select[1]+select[0]*12 == 11:
                        options[11] = False
                    else:
                        options[select[1]+select[0]*12] -= 1
            elif evenement.key == ENTREE:
                if(Option):
                    if select[1] == 12:
                        Option = False
                        mettre_a_jour_options()
                        reinitialiser(True)
                    elif (select[1]+select[0]*12) < len(options) and options[select[1]] < 100:
                        if select[1]+select[0]*12 == 10:
                            options[10] = True
                        elif select[1]+select[0]*12 == 11:
                            options[11] = True
                        else:
                            options[select[1]+select[0]*12] += 1

                elif select[1] == 0:
                    global manche
                    Jeu = True
                    for avion in avions:
                        avion['score'] = 0
                        avion['ajoute_vitesse'] = 0
                        avion['ajoute_inclinaison'] = 0
                        manche = 0
                elif select[1] == 1:
                    Option = True
                    select = [0, 0]
                elif select[1] == 2:
                    Fini = True

            if evenement.key == MENU_BAS:
                select[1] += 1
            elif evenement.key == MENU_HAUT:
                select[1] -= 1
            elif evenement.key == MENU_GAUCHE:
                select[0] -= 1
            elif evenement.key == MENU_DROITE:
                select[0] += 1

def menu_pause():
    global Pause, Pause_delai
    if Pause:
        select[0] %= 3
        largeur = 400
        hauteur = 600
        pygame.draw.rect(fenetre, BLANC, (5, 5, 10, 25))
        pygame.draw.rect(fenetre, BLANC, (20, 5, 10, 25))
        pygame.draw.rect(fenetre, GRIS, (dimensions_fenetre[0]/2 - largeur/2, dimensions_fenetre[1]/2 - hauteur/2, largeur, hauteur))
        police  = pygame.font.Font("police/crochet.otf", 100)
        affiche_message("PAUSE", police, (dimensions_fenetre[0]/2, dimensions_fenetre[1]/2 - 4*hauteur/4 + 380), BLANC)
        police  = pygame.font.Font("police/crochet.otf", 60)

        couleurs = [BLANC, BLANC, BLANC]
        i = 0
        for i in range(3):
            if select[0] == i:
                couleurs[i] = JAUNE
            else:
                couleurs[i] = BLANC

        affiche_message("Continuer", police, (dimensions_fenetre[0]/2, dimensions_fenetre[1]/2 - 3*hauteur/4 + 380), couleurs[0])
        affiche_message("Recommencer", police, (dimensions_fenetre[0]/2, dimensions_fenetre[1]/2 - 2*hauteur/4 + 380), couleurs[1])
        affiche_message("Quitter", police, (dimensions_fenetre[0]/2, dimensions_fenetre[1]/2 - 1*hauteur/4 + 380), couleurs[2])
    elif Pause_delai > 0:
        Pause_delai -= 1
        pygame.draw.polygon (fenetre, BLANC, [(5, 5), (5,30), (30, 17.5)])

def affiche_menu():
    global select, Option
    fenetre.fill(BLEU_CIEL)
    temps = pygame.time.get_ticks()
    if Option:
        select[1] %= 13
        select[0] %= len(options)//12 + 1

        if select[1] == 12:
            dessiner_fleche((FENETRE_LARGEUR//2 - 160, 19*FENETRE_HAUTEUR//20) ,NOIR, 80, 16, 16, 2)
            dessiner_fleche((FENETRE_LARGEUR//2 - 160, 19*FENETRE_HAUTEUR//20) ,VERT, 80, 16, 16)

        else:
            dessiner_fleche((430 + select[0]*FENETRE_LARGEUR//3,  6*FENETRE_HAUTEUR//20 + select[1]*(1*FENETRE_HAUTEUR//20)),NOIR, 80, 16, 16, 2)
            dessiner_fleche((430 + select[0]*FENETRE_LARGEUR//3,   6*FENETRE_HAUTEUR//20 + select[1]*(1*FENETRE_HAUTEUR//20)),VERT, 80, 16, 16)

        police  = pygame.font.Font("police/crochet.otf", 100)
        affiche_message_centre("Options", police, (FENETRE_LARGEUR//2, FENETRE_HAUTEUR//8), 26, 10, NOIR, BLEU)
        police  = pygame.font.Font("police/crochet.otf", 24)

        for i in range(0, len(options)):
            if i > 11:
                j = i%11
                affiche_message(options_noms[i].format(options[i]), police, (FENETRE_LARGEUR//2 + (i//12)*FENETRE_LARGEUR//3, (j+5)*FENETRE_HAUTEUR//20), NOIR)
            else:
                affiche_message(options_noms[i].format(options[i]), police, (FENETRE_LARGEUR//2, (i+6)*FENETRE_HAUTEUR//20), NOIR)

        police  = pygame.font.Font("police/crochet.otf", 36)
        affiche_message_centre("Quitter", police, (FENETRE_LARGEUR//2, 19*FENETRE_HAUTEUR//20), 16, 4, NOIR, ROUGE)

    else:
        delai = 1000
        select[1] %= 3
        police  = pygame.font.Font("police/crochet.otf", 200)
        if( temps%delai <  delai/2 ):
            affiche_message_centre(" AIRPLANES ", police, (FENETRE_LARGEUR//2, FENETRE_HAUTEUR//5), 26, 10, ROUGE, MAUVE)
        else:
            affiche_message_centre(" AIRPLANES ", police, (FENETRE_LARGEUR//2, FENETRE_HAUTEUR//5), 26, 10, VERT, MAUVE)

        dessiner_fleche((50 + 6*FENETRE_LARGEUR//20, 11*FENETRE_HAUTEUR//20 + select[1]*(3*FENETRE_HAUTEUR//20)),NOIR, 80, 16, 16, 2)
        dessiner_fleche((50 + 6*FENETRE_LARGEUR//20, 11*FENETRE_HAUTEUR//20 + select[1]*(3*FENETRE_HAUTEUR//20)),VERT, 80, 16, 16)

        police  = pygame.font.Font("police/crochet.otf", 64)
        affiche_message_centre(" Jouer ", police, (FENETRE_LARGEUR//2, 11*FENETRE_HAUTEUR//20), 16, 4, NOIR, VERT_FONCE)
        affiche_message_centre(" Options ", police, (FENETRE_LARGEUR//2, 14*FENETRE_HAUTEUR//20), 16, 4, NOIR, BLEU)
        affiche_message_centre(" Quitter ", police, (FENETRE_LARGEUR//2, 17*FENETRE_HAUTEUR//20), 16, 4, NOIR, ROUGE)

    pygame.display.flip()
    horloge.tick(10)

def mettre_a_jour_options():
    global VIE_MAX, VITESSE_MAX, PUISSANCE, MANIABILITE, RESISTANCE, TAILLE, BALLE_VITESSE, BALLE_LONGUEUR, BALLE_EPAISSEUR, DELAI_TIR, VITESSE_MIN, MANCHE_MIN, COLLISION, POWER
    VIE_MAX = options[0]
    VITESSE_MAX = options[1]
    VITESSE_MIN = VITESSE_MAX/2
    PUISSANCE = options[2]
    MANIABILITE = options[3]
    RESISTANCE = options[4]
    BALLE_VITESSE = options[5]
    BALLE_LONGUEUR = options[6]
    BALLE_EPAISSEUR = options[7]
    DELAI_TIR = options[8]
    MANCHE_MIN = options[9]
    COLLISION = options[10]
    POWER = options[11]

def affiche_message_centre(texte, police, position, marge, epaisseur, couleur1 = NOIR, couleur2 = BLANC, gras = True, contour = True):
    message = police.render(texte, gras, couleur1)
    message_largeur, message_hauteur = police.size(texte)
    if contour:
        pygame.draw.rect(fenetre, couleur1, (position[0] - message_largeur//2 - marge//2, position[1] - message_hauteur//2 - marge//2, message_largeur + marge, message_hauteur + marge))
        marge -= epaisseur
    pygame.draw.rect(fenetre, couleur2, (position[0] - message_largeur//2 - marge//2, position[1] - message_hauteur//2 - marge//2, message_largeur + marge, message_hauteur + marge))
    fenetre.blit(message, (position[0] - message_largeur//2, position[1] - message_hauteur//2))

def affiche_message(texte, police, position, couleur1, gras=True):
    message = police.render(texte, gras, couleur1)
    message_largeur, message_hauteur = police.size(texte)
    fenetre.blit(message, (position[0] - message_largeur/2, position[1]- message_hauteur/2))

def dessiner_fleche(position, couleur, L, l, c, contour=0):
    dessine_triangle((position[0]+L//2, position[1]), couleur, c, contour)
    pygame.draw.rect(fenetre, couleur, (position[0] - L//2 - contour, position[1] - l//2 - contour, L+2*contour, l+2*contour))

def dessine_triangle(position, couleur, c, contour):
    pt1 = (position[0] - contour, position[1] + c + 2*contour)
    pt2 = (position[0] + 2*c + 2*contour, position[1])
    pt3 = (position[0] - contour, position[1] - c - 2*contour)
    pygame.draw.polygon(fenetre, couleur ,(pt1,pt2,pt3))

def maj_positions():
    global temps
    i = 0
    k = 0
    for avion in avions:
        if avion['vie'] <= 0:
            global t, ori, first
            if first[i]:
                crash.play()
                ori[i] = avion['orientation']
                first[i] = False
            t[i] += 1
            avion['tir_delai'] = 1000

            avion['position'][1] += avion['vitesse']*math.sin(ori[i])+GRAVITE*t[i]*t[i]/1000
            avion['position'][0] += avion['vitesse']*math.cos(ori[i])
            if(math.sin(avion['orientation']) < 0.95):

                if (math.cos(ori[i]) >= 0):
                    avion['orientation'] += PI/120
                else:
                    avion['orientation'] -= PI/120

        else:
            avion['vitesse'] += avion['ajoute_vitesse'] / ((VIE_MAX + RESISTANCE) / (avion['vie'] + RESISTANCE))
            avion['orientation'] += avion['ajoute_inclinaison'] / ((VIE_MAX +RESISTANCE) / (avion['vie'] + RESISTANCE))
            if(avion['vitesse'] > VITESSE_MAX):
                avion['vitesse'] = VITESSE_MAX
            elif(avion['vitesse'] < VITESSE_MIN):
                avion['vitesse'] = VITESSE_MIN
            if(avion['vitesse'] < (VITESSE_MIN + VITESSE_MAX)/2):
                avion['position'][1] += ((VITESSE_MIN + VITESSE_MAX)/2 - avion['vitesse'])*GRAVITE
            avion['position'][0] += avion['vitesse']*math.cos(avion['orientation'])
            avion['position'][1] += avion['vitesse']*math.sin(avion['orientation'])

            if sorti_haut(avion['position'], dimensions_avion[1]):
                avion['vitesse'] -= 0.1
            if sorti_gauche(avion['position'], dimensions_avion[0]):
                avion['position'][0] = FENETRE_LARGEUR + dimensions_avion[0]
            if sorti_droite(avion['position'], dimensions_avion[0]):
                avion['position'][0] = -dimensions_avion[0]
        i += 1

        if(avion['position'][1] > (dimensions_fenetre[1] - hauteur_sol(avion['position'][0], temps_maintenant))):
            avion['vie'] = 0
            avions[(k+1)%2]['score'] += 1
            crash.stop()
            boom.play()
            ajoute_explosion(avion['position'], 1)
            affiche_explosion()
            pygame.display.flip()
            pygame.time.wait(1000)
            reinitialiser()
        k += 1

def maj_balles():
    i = 0
    for avion in avions:
        if(avion['tir_delai'] > 0):
            avion['tir_delai'] -= 1
        if(avion['tir_delai'] == 0):
            avion['balles'] += [((avion['position'][0], avion['position'][1]), avion['orientation'])]
            avion['tir_delai'] = DELAI_TIR
            tir.play()
        j = 0
        for balle in avion['balles']:
            avions[i]['balles'][j] = ((balle[0][0] + BALLE_VITESSE*math.cos(balle[1]), (balle[0][1] + BALLE_VITESSE*math.sin(balle[1]))), balle[1])
            if sorti_fenetre(balle[0], dimensions_avion[0]//2):
                del(avions[i]['balles'][j])
            j += 1
        i += 1

def affiche_avions():
    for avion in avions:
        avion['rectangle'], image = rotation_centre(avion['image'], avion['rectangle'], avion['orientation'] + PI/20)
        position = (avion['position'][0] - avion['rectangle'][0]/2, avion['position'][1] - avion['rectangle'][1]/2)
        fenetre.blit(image, (int(position[0]), int(position[1])))

def affiche_balles():
    for avion in avions:
        for balle in avion['balles']:
            l = 1
            while(l < BALLE_LONGUEUR):
                pygame.draw.circle(fenetre, GRIS, (int(balle[0][0] - l*math.cos(balle[1])), int(balle[0][1] - l*math.sin(balle[1]))), BALLE_EPAISSEUR)
                l += 1
            pygame.draw.circle(fenetre, JAUNE, (int(balle[0][0]), int(balle[0][1])), BALLE_EPAISSEUR)
            pygame.draw.circle(fenetre, JAUNE, (int(balle[0][0]), int(balle[0][1])), BALLE_EPAISSEUR)

def affiche_nuage():
    i = 0
    for nuage in nuages:
        nuages[i] = (nuage[0]-1, nuage[1])
        fenetre.blit(IMAGE_NUAGE, (int(nuage[0]), int(nuage[1])))
        if sorti_horizontal(nuage, dimensions_nuage[0]):
            nuages[i] = (dimensions_fenetre[0] + dimensions_nuage[0], nuage[1])
        i += 1

def affiche_vies():
    for avion in avions:
        if(avion['vie'] < 0):
            avion['vie'] = 0
        if(avion['vie_delai'] >= 0):
            pygame.draw.rect(fenetre, NOIR, (avion['position'][0] - 26, avion['position'][1] - 1 - dimensions_avion[0]//1.5, 52, 10))
            pygame.draw.rect(fenetre, ROUGE, (avion['position'][0] - 25, avion['position'][1] - dimensions_avion[0]//1.5, 50, 8))
            pygame.draw.rect(fenetre, VERT, (avion['position'][0] - 25, avion['position'][1] - dimensions_avion[0]//1.5, 50*avion['vie']//VIE_MAX, 8))
            avion['vie_delai'] -= 1

def dessiner_sol1(temps):
    for x in range(dimensions_fenetre[0]):

        y = hauteur_sol(x, temps)
        pygame.draw.line(fenetre, VERT_FONCE, (x, dimensions_fenetre[1] - y), (x, dimensions_fenetre[1]))

def dessiner_sol2(temps):
    for x in range(dimensions_fenetre[0]):
        y = hauteur_sol(x, temps, 120, 100, 30)
        pygame.draw.line(fenetre, HERBE, (x, dimensions_fenetre[1] - y), (x, dimensions_fenetre[1]))

def score():
    global manche, MANCHE_MIN
    police = pygame.font.Font("police/crochet.otf", 42)
    if (manche+1) >= MANCHE_MIN:
        affiche_message("Manche finale", police, (FENETRE_LARGEUR//2, 22), NOIR)
    else:
        affiche_message("Manche {:d}".format(manche+1), police, (FENETRE_LARGEUR//2, 22), NOIR)
    affiche_message(":".format(avions[0]['score'], ), police, (FENETRE_LARGEUR//2, 58), NOIR)
    affiche_message("{:d}".format(avions[0]['score'], ), police, (FENETRE_LARGEUR//2 + 30, 60), ROUGE)
    affiche_message("{:d}".format(avions[1]['score'], ), police, (FENETRE_LARGEUR//2 - 30, 60), VERT)

def collision():
    global COLLISION
    for avion1 in avions:
        j = 0
        for power in power_up_list:
            d3 = distance2(power, avion1['position'])
            if(avion1['vie'] > 0 and d3 < ((dimensions_avion[1]/1.5)**2)):
                global DELAI_POWER_UP
                DELAI_POWER_UP = random.randint(200, 1000)
                del power_up_list[j]
                avion1['vie'] += VIE_MAX//4
                if avion1['vie'] > VIE_MAX:
                    avion1['vie'] = VIE_MAX
                avion1['vie_delai'] = 90
            j += 1
        for avion2 in avions:
            if COLLISION:
                d2 = distance2(avion1['position'], avion2['position'])
                if(avion1['image'] != avion2['image'] and avion1['vie'] > 0 and d2 < ((dimensions_avion[1]/1.5)**2)):
                    boom.play()
                    avion1['vie'] = 0
                    avion2['vie'] = 0
                    avion1['vie_delai'] = 90
                    avion2['vie_delai'] = 90
                    inter = ((avion1['position'][0]+avion2['position'][0])//2, (avion1['position'][1]+avion2['position'][1])//2)
                    ajoute_explosion(inter, 30)
            i = 0
            for balle in avion1['balles']:
                d = distance2(balle[0], (avion2['position'][0], avion2['position'][1]))
                if(avion1['image'] != avion2['image'] and d < ((dimensions_avion[1]/1.5)**2)):
                    del(avion1['balles'][i])
                    degat_avion(avion2)
                i += 1

def ajoute_explosion(position, duree):
    global explosions
    explosions += [((position[0] - dimensions_explo[0]//2, position[1] - dimensions_explo[1]//2), duree)]

def affiche_explosion():
    global explosions
    i = 0
    for explosion in explosions:
        if explosion[1] > 0:
            fenetre.blit(IMAGE_EXPLO, (explosion[0][0], explosion[0][1]))
            explosions[i] = (explosion[0], explosion[1] - 1)
        else:
            del(explosions[i])
        i += 1

def degat_avion(avion):
    avion['vie_delai'] = 90
    avion['vie'] -= 1
    avion['tir_delai'] = 60

def nouvel_avion(image):
    return {
    'image' : image,
    'position' : [],
    'vitesse' : VITESSE_MAX,
    'orientation' : 0,
    'rectangle' : image.get_size(),
    'ajoute_vitesse' : 0,
    'ajoute_inclinaison' : 0,
    'balles' : [],
    'tir_delai' : DELAI_TIR,
    'vie' : VIE_MAX,
    'vie_delai' : 0,
    'score' : 0
    }

def sorti_fenetre(point, marge=0):
    if sorti_vertical(point, marge) or sorti_horizontal(point, marge):
        return True
    else:
        return False

def sorti_vertical(point, marge=0):
    if(sorti_bas(point, marge) or sorti_haut(point, marge)):
        return True
    else:
        return False

def sorti_horizontal(point, marge=0):
    if(sorti_gauche(point, marge) or sorti_droite(point, marge)):
        return True
    else:
        return False

def sorti_droite(point, marge=0):
    if(point[0] > FENETRE_LARGEUR + marge):
        return True
    else:
        return False

def sorti_gauche(point, marge=0):
    if(point[0] < -marge):
        return True
    else:
        return False

def sorti_haut(point, marge=0):
    if(point[1] < -marge):
        return True
    else:
        return False

def sorti_bas(point, marge=0):
    if(point[1] > FENETRE_HAUTEUR + marge):
        return True
    else:
        return False

def rotation_centre(image, rectangle, angle):
    image2 = pygame.transform.rotate(image, -angle*180/PI)
    rectangle2 = image2.get_size()
    return rectangle2, image2

def distance2(pt1, pt2):
    dh = pt1[0] - pt2[0]
    dv = pt1[1] - pt2[1]
    d2 = dh*dh + dv*dv
    return d2

def hauteur_sol(x, temps=0, hauteur = 40, etireX = 50, etireY = 20):
    alpha = (-x - temps)/ etireX
    y = etireY * math.exp(math.cos(alpha)) / math.e + hauteur
    return y

def fait_nuage():
    global nuages
    i = 0
    while (i < 14):
        x = random.randint(-dimensions_nuage[0], dimensions_fenetre[0] + dimensions_nuage[0])
        y = random.randint(0, dimensions_fenetre[1]//2)
        nuages += [(x, y)]
        i += 1

def reinitialiser(new=False):
    global init, manche, Fini, t, first, ori, Jeu, power_up_list
    t = [0, 0]
    ori = [0, 0]
    first = [True, True]
    power_up_list = []

    avions[0]['position'] = [3*FENETRE_LARGEUR/4, FENETRE_HAUTEUR/2]
    avions[0]['orientation'] = PI
    avions[1]['position'] = [FENETRE_LARGEUR/4, FENETRE_HAUTEUR/2]
    avions[1]['orientation'] = 0
    for avion in avions:
        avion['vitesse'] = VITESSE_MAX
        avion['vie'] = VIE_MAX
        avion['vie_delai'] = 0
        avion['balles'] = []
        avion['tir_delai'] = 120
        if new:
            avion['score'] = 0

    if new:
        manche = 0
    else:
        manche += 1
        if(manche >= MANCHE_MIN and abs(avions[0]['score'] - avions[1]['score']) > 0):
            Jeu = False
            manche = 0
            police  = pygame.font.Font("police/crochet.otf", 150)
            if avions[0]['score'] > avions[1]['score']:
                affiche_message("Le joueur 1 a gagné !", police, (dimensions_fenetre[0]/2, dimensions_fenetre[1]/3), ROUGE)
            elif avions[1]['score'] > avions[0]['score']:
                affiche_message("Le joueur 2 a gagné !", police, (dimensions_fenetre[0]/2, dimensions_fenetre[1]/3), VERT_FONCE)
            else:
                affiche_message("Egalité !", police, (dimensions_fenetre[0]/2, dimensions_fenetre[1]/3), NOIR)
            pygame.display.flip()
            pygame.time.wait(2000)
    init = True

def power_up():
    global DELAI_POWER_UP, power_up_list
    if DELAI_POWER_UP > 0:
        DELAI_POWER_UP -= 1
    else:
        DELAI_POWER_UP = 1200
        ajoute_power_up()
    i = 0
    for power in power_up_list:
        power_up_list[i] = (power[0], power[1]+1)
    i += 1

def ajoute_power_up():
    global power_up_list
    pos = (random.randint(50, dimensions_fenetre[0]-50), -50)
    power_up_list += [pos]

def affiche_power_up():
    for power in power_up_list:
        fenetre.blit(IMAGE_CLE, (power[0]-dimensions_cle[0]//2, power[1]-dimensions_cle[1]//2))


# INITIALISATION

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.font.init()
pygame.init()

dimensions_fenetre = (FENETRE_LARGEUR, FENETRE_HAUTEUR)
fenetre = pygame.display.set_mode(dimensions_fenetre)
pygame.display.set_caption("Airplanes")

crash = pygame.mixer.Sound("sons/crash.wav")
boom = pygame.mixer.Sound("sons/explosion.wav")
tir = pygame.mixer.Sound("sons/tir.wav")
tir.set_volume(0.1)
pygame.mixer.music.load("sons/RGT.wav")
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)

IMAGE_AVION_VERT_ORIGINE = pygame.image.load('images/aircraft_green.png').convert_alpha(fenetre)
IMAGE_AVION_ROUGE_ORIGINE = pygame.image.load('images/aircraft_red.png').convert_alpha(fenetre)
dimensions_avion = IMAGE_AVION_VERT_ORIGINE.get_size()
rapport = 100/TAILLE
dimensions_avion = (dimensions_avion[0]/rapport, dimensions_avion[1]/rapport)
IMAGE_AVION_VERT = pygame.transform.scale(IMAGE_AVION_VERT_ORIGINE, (int(dimensions_avion[0]), int(dimensions_avion[1])))
IMAGE_AVION_ROUGE = pygame.transform.scale(IMAGE_AVION_ROUGE_ORIGINE, (int(dimensions_avion[0]), int(dimensions_avion[1])))

IMAGE_NUAGE = pygame.image.load('images/cloud.png').convert_alpha(fenetre)
dimensions_nuage = IMAGE_NUAGE.get_size()
dimensions_nuage = (dimensions_nuage[0]*2, dimensions_nuage[1]*2)
IMAGE_NUAGE = pygame.transform.scale(IMAGE_NUAGE, (dimensions_nuage[0], dimensions_nuage[1]))

IMAGE_EXPLO = pygame.image.load('images/explo.png').convert_alpha(fenetre)
dimensions_explo = IMAGE_EXPLO.get_size()
dimensions_explo = (dimensions_explo[0]/(3*rapport), dimensions_explo[1]/(3*rapport))
IMAGE_EXPLO = pygame.transform.scale(IMAGE_EXPLO, (int(dimensions_explo[0]), int(dimensions_explo[1])))

IMAGE_CLE = pygame.image.load('images/cle.png')
dimensions_cle = IMAGE_CLE.get_size()
dimensions_cle = (dimensions_cle[0]/15, dimensions_cle[1]/15)
IMAGE_CLE = pygame.transform.scale(IMAGE_CLE, (int(dimensions_cle[0]), int(dimensions_cle[1])))

explosions = []
nuages = []
avions = []
avions += [nouvel_avion(IMAGE_AVION_ROUGE)]
avions += [nouvel_avion(IMAGE_AVION_VERT)]

options = [VIE_MAX, VITESSE_MAX, PUISSANCE, MANIABILITE, RESISTANCE, BALLE_VITESSE, BALLE_LONGUEUR, BALLE_EPAISSEUR, DELAI_TIR, MANCHE_MIN, COLLISION, POWER]
options_noms = ["Vie              : {:d}", "Vitesse max      : {:d}", "Puissance        : {:d}", "Maniabilite      : {:d}", "Resistance       : {:d}", "Vitesse balles   : {:d}", "Longueur balles  : {:d}", "Epaisseur balles : {:d}", "Delai entre tirs : {:d}", "Manche           : {:d}","Collision        : {}", "Power up        : {}"]

DELAI_POWER_UP = 500
power_up_list = []
Fini = False
Jeu = False
Option = False
Pause = False
Pause_delai = 0

select = [0, 0]

horloge = pygame.time.Clock()

reinitialiser(True)
fait_nuage()

while not Fini:
    if not Jeu:
        affiche_menu()
        gerer_entree_menu()
    else:
        temps_maintenant = pygame.time.get_ticks()
        gerer_entree()
        if not Pause:
            maj_positions()
            maj_balles()
            if POWER:
                power_up()
        fenetre.fill(BLEU_CIEL)
        dessiner_sol2(temps_maintenant/20)
        affiche_nuage()
        affiche_vies()
        affiche_balles()
        affiche_avions()
        affiche_power_up()
        dessiner_sol1(temps_maintenant/10)
        collision()
        affiche_explosion()
        menu_pause()
        score()
        horloge.tick(IMAGES_PAR_SECONDE)
        pygame.display.flip()
        if init and Jeu:
            init = False
            pygame.time.wait(1000)

pygame.display.quit()
pygame.quit()
exit()
