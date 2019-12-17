#!/usr/bin/env python3

# 'παιδεύω'
# 'ἔχω'

diphtongues= ['αι','αυ','ει','ευ','οι','ου','ηυ','υι']
voyelles_sans_dia= ['α','ε','η','ι','ο','υ','ω']

finales_ind_pres_act = ['ω','εις','ει','ομεν','ετε','ουσι']
finales_ind_imp_act = ['ον','ες','ε','ομεν','ετε','ον']

no_diacritic={}
def _gen_no_diacritic():
    no_diacritic_temp = {
        'α': ['α','ἀ','ἁ','ᾀ','ᾁ','ᾳ','ἂ','ἃ','ἄ','ἅ','ἆ','ἇ','ὰ','ᾶ','ᾂ','ᾃ','ᾄ','ᾅ','ᾆ','ᾇ','ᾲ','ᾷ','ᾴ','ά'],
        'ε': ['ε', 'ἐ','ἑ','έ','ὲ','ἕ','ἔ','ἓ','ἒ'],
        'η': ['η','ή', 'ἠ', 'ἡ', 'ἢ', 'ἣ', 'ἤ', 'ἥ', 'ἦ', 'ἧ', 'ὴ', 'ῆ', 'ῃ', 'ᾐ', 'ᾑ', 'ᾒ', 'ᾓ', 'ᾔ', 'ᾕ', 'ᾖ', 'ᾗ', 'ῂ', 'ῇ', 'ῄ'],
        'ι': ['ι', 'ί', 'ἰ', 'ἱ', 'ἲ', 'ἳ', 'ἴ', 'ἶ', 'ἵ', 'ἷ', 'ὶ', 'ῖ'],
        'ο': ['ο', 'ό','ὀ','ὁ','ὂ','ὃ','ὄ','ὅ','ὸ'],
        'υ': ['υ', 'ύ','ὐ','ὑ','ὒ','ὓ','ὔ','ὕ','ὖ','ὗ','ὺ','ῦ'],
        'ω': ['ω', 'ώ','ὠ','ὡ','ὢ','ὣ','ὤ','ὥ','ὦ','ὧ','ὼ','ῶ','ῳ','ᾠ','ᾡ','ᾢ','ᾣ','ᾤ','ᾥ','ᾦ','ᾧ','ῲ','ῷ','ῴ']
    }
    ret = {}
    for k,v in no_diacritic_temp.items():
        for i in v:
            ret[i] = k
    return ret
no_diacritic = _gen_no_diacritic()

def radicalisateur(mot):
    if mot[-1]=='ω':
        mot=mot[:-1]
        return mot
    
def is_voyelle(lettre):
    return lettre in no_diacritic
    
def is_diphtongue(lettres):
    return lettres in diphtongues

def dediacritique(mot):
    nouveau_mot=list(mot)
    for i in range(len(mot)):
        if is_voyelle(mot[i]):
            nouveau_mot[i]=no_diacritic[mot[i]]
            continue
        else:
            nouveau_mot[i]=mot[i]
            continue
    else: mot =''.join(nouveau_mot)
    return mot

def ajout_finale(radical,finales):
    retour = ['']*len(finales)
    for i in range(len(finales)):
        retour[i]=radical+finales[i]
    else: return retour

def contract_aug(radical):
    if radical=='α' or radical=='η': return 'ἠ'
    elif radical=='αι': return 'ᾐ'
    elif radical=='ει' or radical=='ε' or radical=='ι': return 'εἰ'
    elif radical=='ου' or radical=='ο': return 'οὐ'
    elif radical=='ω': return 'ὠ'
    elif radical=='οι': return 'οἰ'
    elif radical=='υ': return 'ἐυ'

def resprit(lettre):
    lettre= chr(7936+(16*voyelles_sans_dia.index(lettre)))
    return lettre

def raccent(lettre):
    lettre = chr(ord(lettre)+5)
    return lettre

#def ajout_accent(tableau):
#    for x in range(len(tableau)):
#        nouveau_mot=list(tableau[x])
#        if nouveau_mot[-1]=='η' or nouveau_mot[-1]=='ω' or nouveau_mot[-2] in diphtongues:
#                z=0
#                i=0
#                while i<3 or z>(-(len(nouveau_mot))-1):
#                    if nouveau_mot[z-1] in voyelles or nouveau_mot[z-2] in diphtongues:
#                        i=i+1
#                        z=z-1
#                    else: z=z-1
#                else: nouveau_mot[z]=raccent(nouveau_mot[z])
#        else:
#            z=0
#            while i<4 or z>-(len(nouveau_mot)):
#                if nouveau_mot[z-1] in voyelles or nouveau_mot[z-2] in diphtongues:
#                        i=i+1
#                        z=z-1
#                else: z=z-1
#            else: nouveau_mot[z]=raccent(nouveau_mot[z])
#    else: return tableau

def ajout_esprit(tableau):
    for x in range(len(tableau)):
        tableau[x] = resprit(tableau[x][0])+tableau[x][1:]
    else: return tableau
    
    
def gen_pres(mot):
    radical = radicalisateur(dediacritique(mot))
    tableauPres = ajout_finale(radical,finales_ind_pres_act)
    if is_voyelle(radical[0]):
        tableauPres = ajout_esprit(tableauPres)
    tableau_pres = ajout_accent(tableauPres)
    return tableauPres

def add_augment(tableau,radical):
    if is_voyelle(radical[0]):
      if is_diphtongue(radical[:1]):
        for x in range(len(tableau)):
          tableau[x]=contract_aug(radical[:1])+tableau[x][2:]
        else: return tableau
      else:
        for x in range(len(tableau)):
          tableau[x]=contract_aug(radical[0])+tableau[x][1:]
        else: return tableau
    else:
      for x in range(len(tableau)):
        tableau[x]='ἐ'+tableau[x]
      else: return tableau

def gen_imp(mot):
    radical = radicalisateur(dediacritique(mot))
    tableauImp = ajout_finale(radical,finales_ind_imp_act)
    tableauImp = add_augment(tableauImp,radical)
    return tableauImp
