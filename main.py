import translator as tr
import dictionary as diz
t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("filename.txt")
    dd = diz.Dictionary(t.dizionario)

    t.printMenu()

    txtIn = input()

    # Add input control here!
    if txtIn in ('1', '2', '3', '4', '5'):
        if int(txtIn) == 1:
            print()
            txtIn = input()
            continue
        if int(txtIn) == 2:
            continue
        if int(txtIn) == 3:
            continue
        if int(txtIn) == 4:
            continue
        if int(txtIn) == 5:
            break
    else:
        print('\nAttenzione. Scelta non valida ')