'''Začínáš s 0 body.
Počítač v každém kole vypíše, kolik máš bodů, a zeptá se tě, jestli chceš pokračovat.
Pokud odpovíš „ne“, hra končí.
Pokud odpovíš „ano“, počítač „otočí kartu“ (náhodně vybere číslo od 2 do 10), vypíše její hodnotu a přičte ji k bodům.
Pokud máš víc než 21 bodů, prohráváš.
Cílem hry je získat co nejvíc bodů, ideálně 21.'''

from random import randrange
cislo = randrange(22)

print('Vase cislo je:', cislo,'.')
pokracovani = input('Chcete pokracovat?')
finalni_cislo = ''

if pokracovani == 'ano':
    while finalni_cislo != 21 or finalni_cislo > 21:
        
        i = randrange(2,10)
        print('Další číslo je:',i)
        finalni_cislo = i + cislo
        print('Tvé finální číslo je:',finalni_cislo)
        if finalni_cislo > 21:
            print('Prohráls!')
        elif finalni_cislo == 21:
            print('Ty bláho, ty máš štěstí!')
        else:
            print('Dobrá hra :)')
        break
else:
    print('Hra konci.')
