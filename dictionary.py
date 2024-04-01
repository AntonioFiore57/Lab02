#
class Dictionary:
    def __init__(self):
        self.dizionario = dict()


    def addWord(self,parola_aliena, parola_italiana):
        if parola_aliena not in self.dizionario:
            self.dizionario[parola_aliena] = [parola_italiana]
        else:
            self.dizionario[parola_aliena].append(parola_italiana)

    def translate(self, parola_aliena):
        lista_parole_italiane = self.dizionario.get(parola_aliena, [])
        parole_italiane = ', '.join(lista_parole_italiane)
        return parole_italiane

    def translateWordWildCard(self):
        pass

