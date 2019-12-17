#!/usr/bin/env python3

# 'παιδεύω'
# 'ἔχω'
no_diacritic= {
    'ἀ':'α','ἁ':'α','α':'α','ᾀ':'α','ᾁ':'α','ᾳ':'α','ἂ':'α','ἃ':'α','ἄ':'α','ἅ':'α','ἆ':'α','ἇ':'α','ὰ':'α','ᾶ':'α','ᾂ':'α','ᾃ':'α','ᾄ':'α','ᾅ':'α','ᾆ':'α','ᾇ':'α','ᾲ':'α','ᾷ':'α','ᾴ':'α','ά':'α',
    'ἐ':'ε','ἑ':'ε','ε':'ε','έ':'ε','ὲ':'ε','ἕ':'ε','ἔ':'ε','ἓ':'ε','ἒ':'ε',
    'η':'η','ή':'η','ἠ':'η','ἡ':'η','ἢ':'η','ἣ':'η','ἤ':'η','ἥ':'η','ἦ':'η','ἧ':'η','ὴ':'η','ῆ':'η','ῃ':'η','ᾐ':'η','ᾑ':'η','ᾒ':'η','ᾓ':'η','ᾔ':'η','ᾕ':'η','ᾖ':'η','ᾗ':'η','ῂ':'η','ῇ':'η','ῄ':'η',
    'ι':'ι','ί':'ι','ἰ':'ι','ἱ':'ι','ἲ':'ι','ἳ':'ι','ἴ':'ι','ἶ':'ι','ἵ':'ι','ἷ':'ι','ὶ':'ι','ῖ':'ι',
    'ο':'ο','ό':'ο','ὀ':'ο','ὁ':'ο','ὂ':'ο','ὃ':'ο','ὄ':'ο','ὅ':'ο','ὸ':'ο',
    'υ':'υ','ύ':'υ','ὐ':'υ','ὑ':'υ','ὒ':'υ','ὓ':'υ','ὔ':'υ','ὕ':'υ','ὖ':'υ','ὗ':'υ','ὺ':'υ','ῦ':'υ',
    'ω':'ω','ώ':'ω','ὠ':'ω','ὡ':'ω','ὢ':'ω','ὣ':'ω','ὤ':'ω','ὥ':'ω','ὦ':'ω','ὧ':'ω','ὼ':'ω','ῶ':'ω','ῳ':'ω','ᾠ':'ω','ᾡ':'ω','ᾢ':'ω','ᾣ':'ω','ᾤ':'ω','ᾥ':'ω','ᾦ':'ω','ᾧ':'ω','ῲ':'ω','ῷ':'ω','ῴ':'ω'
    }
diphtongues= ['αι','αυ','ει','ευ','οι','ου','ηυ','υι']
voyelles=['ω','ώ','ὠ','ὡ','ὢ','ὣ','ὤ','ὥ','ὦ','ὧ','ὼ','ῶ','ῳ','ᾠ','ᾡ','ᾢ','ᾣ','ᾤ','ᾥ','ᾦ','ᾧ','ῲ','ῷ','ῴ','υ','ύ','ὐ','ὑ','ὒ','ὓ','ὔ','ὕ','ὖ','ὗ','ὺ','ῦ','ο','ό','ὀ','ὁ','ὂ','ὃ','ὄ','ὅ','ὸ','ἀ','ἁ','α','ᾀ','ᾁ','ᾳ','ἂ','ἃ','ἄ','ἅ','ἆ','ἇ','ὰ','ᾶ','ᾂ','ᾃ','ᾄ','ᾅ','ᾆ','ᾇ','ᾲ','ᾷ','ᾴ','ά','ἐ','ἑ','ε','έ','ὲ','ἕ','ἔ','ἓ','ἒ','η','ή','ἠ','ἡ','ἢ','ἣ','ἤ','ἥ','ἦ','ἧ','ὴ','ῆ','ῃ','ᾐ','ᾑ','ᾒ','ᾓ','ᾔ','ᾕ','ᾖ','ᾗ','ῂ','ῇ','ῄ']
finales_ind_pres_act = ['ω','εις','ει','ομεν','ετε','ουσι']
finales_ind_imp_act = ['ον','ες','ε','ομεν','ετε','ον']

def radicalisateur(mot):
    if mot[-1]=='ω':
        mot=mot[:-1]
        return mot
    
def is_voyelle(lettre):
    return lettre in voyelles
    
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

def gen_pres(mot):
    radical = radicalisateur(dediacritique(mot))
    tableauPres = ajout_finale(radical,finales_ind_pres_act)
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
