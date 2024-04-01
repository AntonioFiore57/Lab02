import dictionary as diz
import string

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
        # controllo sulle parole inserite
        ok = True
        for i in range(len(entry)):
            if not self._parolaOK(entry[i]):
                ok = False
                break
        if not ok:
            raise ValueError(f"Elemento {i} non valido")
        parola_aliena, *parole_italiane = entry
        for parola in parole_italiane:
            self.dizionario.addWord(parola_aliena, parola)

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        # controllo sulla parola inserita
        if self._parolaOK(query):
            parole_italiane = self.dizionario.translate(query)
            if parole_italiane != '':
                print(query,'-->', parole_italiane)


            else:
                print(f"\nNon conosco la parola Klingon {query}")
        else:
            raise ValueError("Parola inserita non valida")
        return None

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
            for parola_aliena, parole_italiane in self.dizionario.dizionario.items():
                print(f"{parola_aliena:20}->{','.join(parole_italiane)}")
        else:
            print("\nNon ci sono voci")
    def _parolaOK(self, parola):
        ok = True
        for c in parola:
            if c not in string.ascii_lowercase:
                ok=False
                break
        return  ok

