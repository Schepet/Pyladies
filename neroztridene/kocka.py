kocka = ''
while kocka != 'ano' and kocka != 'ne':
    
    kocka = input("Mas doma kocku?")

    if kocka == 'ne':
        print("Chyba!Pořiď si ji.")
    elif kocka == 'ano':
        print('Správná volba :)')
    else:
        print('Nesprávná odpověď, zadej ano nebo ne.')

