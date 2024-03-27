class Translator:

    def __init__(self):
        self.dizionario = []
        pass

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open('dict', 'r', encoding='utf-8') as f_in:
            for riga in f_in:
                voci=riga.strip().split()
                self.dizionario.append(voci[0], voci[1])


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass