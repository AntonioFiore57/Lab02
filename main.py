import translator as tr
# import dictionary as diz
t = tr.Translator()


dizionario_alieno_italiano = t.loadDictionary('dictionary.txt')

while(True):

    t.printMenu()

    txtIn = input('\nInserisci la tua scelta: ')

    # Add input control here!
    if txtIn in ('1', '2', '3', '4', '5'):
        if int(txtIn) == 1:
            print('\n1. Lavori in corso ....')
            # txtIn = input()
            continue
        if int(txtIn) == 2:
            print('\n2. Lavori in corso ....')
            continue
        if int(txtIn) == 3:
            print('\n3. Lavori in corso ....')
            continue
        if int(txtIn) == 4: # stampa tutto il dizionario
            print('\nContenuto del dizionario Klinkon/Italiano')
            t.print_dictionary(dizionario_alieno_italiano)
            input('\nPremi INVIO per continuare ....')
            continue
        if int(txtIn) == 5:
            break
    else:
        print('\nAttenzione. Scelta non valida ')

print('\n*** Finito ***')