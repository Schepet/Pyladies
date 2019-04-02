'''Napiš tyto programy. Každý z nich bude mít na vstupu řetězec s rodným číslem a nějak ho
zanalyzuje:
(a) Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vypíše True nebo False)
(b) Je dělitelné jedenácti? (vypíše True nebo False)
(c) Jaké datum narození je v čísle zakódováno? (vypíše trojici čísel – den, měsíc, rok)
(d) Jaké pohlaví je v čísle zakódováno? (vypíše 'muž' nebo 'žena')
Pro účely úkolu stačí, když bude program umět zpracovat čísla vydávaná od roku 1985.
Reálná rodná čísla můžou být složitější :)
8. Napiš program který se uživatele zeptá na rodné číslo a vypíše, zda zadal rodné
číslo správně (Využije výsledky z úkolu 7).
'''
import datetime 
r_c = input('Vloz sve rodne cislo:')
prvni_cast = r_c[0:6]
druha_cast = r_c[7:11]
#print(prvni_cast)
r_c = prvni_cast + '/' + druha_cast
cisla = '0123456789' + '/'

if len(prvni_cast) == 6:
    r_c = True
    print('Splnuje delku.')
elif len(r_c) != 6:
    r_c = False
else:
    print('Zkus to znovu prosim.')
if len(druha_cast) == 4:
    druha_cast = True
    print('V poho.')
elif len(druha_cast) != 4:
    druha_cast = False
else: 
    print('Znova pls.')
if r_c % 11:
    r_c = True
    print('Zadarilo se.')
else:
    print('Spatne zadano!')


'''if cisla in r_c[0:5]:
    r_c = True
    print('Splnuje format.')
else:
    print('Napis to v jinem formatu.')
if r_c[2] == 5:
    print('Jsi zena!')
elif r_c[2] == 0:
    print("Jsi muz!")
else:
    print('Napis to prosim znova.')'''

