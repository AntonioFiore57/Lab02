import translator as tr
# import dictionary as diz
t = tr.Translator()
t.loadDictionary('dictionary.txt')

while(True):

    t.printMenu()

    txtIn = input('\nInserisci la tua scelta: ')

    # Add input control here!
    if txtIn in ('1', '2', '3', '4', '5'):
        if int(txtIn) == 1: # Aggiungi nuova parola
            txtIn = input("\nQuale parola vuoi aggiungere? --> ")
            txtIn = txtIn.lower()
            parole = txtIn.split()
            parola_aliena, *parole_italiano = parole
            print(parola_aliena, ','.join(parole_italiano))
            try:
                parole = tuple(parole)
                t.handleAdd(parole)
            except ValueError as ee:
                print(ee)

            continue
        if int(txtIn) == 2: #  Cerca una traduzione
            parola_aliena = input("\nInserisci la parola aliena da tradurre: ")
            parola_aliena = parola_aliena.lower()
            try:
                t.handleTranslate(parola_aliena)
            except ValueError as ee:
                print(ee)

            continue
        if int(txtIn) == 3: # Cerca con wildcard
            print('\nRicerca con wildcard')
            parola_aliena = input("\nInserisci la parola aliena da tradurre: ")
            parola_aliena = parola_aliena.lower()
            try:
                t.handleWildCard(parola_aliena)
            except ValueError as ee:
                print(ee)

            continue
        if int(txtIn) == 4: # stampa tutto il dizionario
            print('\nContenuto del dizionario Klinkon/Italiano')
            t.print_dictionary()
            input('\nPremi INVIO per continuare ....')
            continue
        if int(txtIn) == 5:
            break
    else:
        print('\nAttenzione. Scelta non valida ')

print('\n*** Finito ***')