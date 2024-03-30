import dictionary as diz
class Translator:

    def __init__(self):
        self.dizionario =diz.Dictionary()

        pass

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. stampa tutto il dizionario
        # 5. exit
        menu = '\n' + 40*"-" + '\n'
        menu += '\tTraduttore Klingon - Italiano'
        menu += '\n' + 40 * "-" + '\n'
        menu += '1. Aggiungi nuova parola\n'
        menu += '2. Cerca una traduzione\n'
        menu += '3. Cerca con wildcard\n'
        menu += '4. stampa tutto il dizionario\n'
        menu += '5. exit\n'
        print(menu)

    def loadDictionary(self, dict):

        # dict is a string with the filename of the dictionary
        with open('dictionary.txt', 'r', encoding='utf-8') as f_in:
            for riga in f_in:
                riga = riga.strip()
                campi=riga.split()

                self.dizionario.addWord(campi[0], campi[1])
        return None



    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass

    def print_dictionary(self):
        """
        viene stampato a a console self.dizionario.
        si gestesce da questo metodo la visualizzazione
        del dizionario
        :return: None
        """
        if len(self.dizionario.dizionario) != 0:
            for parola_aliena, parola_italiana in self.dizionario.dizionario.items():
                print(f"{parola_aliena:20}->{parola_italiana:20}")
        else:
            print("\nNon ci sono voci")