from random import randrange
cislo = randrange(3)
tahy = ['kamen', 'nuzky', 'papir']
tah_pocitace = tahy[cislo]
print('tah pocitace:',tahy[cislo])
tah_cloveka = input('kamen, nuzky, nebo papir?')
if tah_cloveka == tah_pocitace:
    print('Plichta')
elif tah_pocitace == 'kamen' and tah_cloveka == 'nuzky':
    print('pocitac vyhral')
elif tah_pocitace == 'kamen' and tah_cloveka == 'papir':
    print('vyhral jsi')
elif tah_pocitace == 'nuzky' and tah_cloveka == 'papir':
    print('pocitac vyhral')
elif tah_pocitace == 'nuzky' and tah_cloveka == 'kamen':
    print('vyhral jsi')
elif tah_pocitace == 'papir' and tah_cloveka == 'kamen':
    print('pocitac vyhral')
elif tah_pocitace == 'papir' and tah_cloveka == 'nuzky':
    print('pocitac vyhral')
else:
    print('tahni znova')