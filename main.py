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

            parola_aliena, parola_italiana = txtIn.split()
            print(parola_aliena, parola_italiana)
            t.handleAdd((parola_aliena, parola_italiana))
            continue
        if int(txtIn) == 2: #  Cerca una traduzione
            parola_aliena = input("\nInserisci la parola aliena da tradurre: ")
            t.handleTranslate(parola_aliena)

            continue
        if int(txtIn) == 3:
            print('\n3. Lavori in corso ....')
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