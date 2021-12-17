from arbre_decision_comp import table, cons_abr, luka, compression, dot, dot_py

###############################    Partie III  Arbre de d ́ecision et ROBDD     ###########################

'''Question 3.10'''


def compression_bdd(Noeud):

    if isinstance(Noeud.lukaval,bool):
        return Noeud
    else:
        Noeud.gauche = compression_bdd(Noeud.gauche)
        Noeud.droit = compression_bdd(Noeud.droit)

        if(Noeud.gauche.get_id()==Noeud.droit.get_id()):
            return Noeud.get_droit()

        return Noeud


##################################         Fin  Partie III         ###################################

####TEST4 compression_bdd()####
'''
abd = cons_abr(table(38,8))
luka(abd)
abd = compression({},abd)
abd = compression_bdd(abd)
dot(abd)
dot_py(abd)
'''

