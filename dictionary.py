#
class Dictionary:
    def __init__(self):
        self.dizionario = dict()


    def addWord(self,parola_aliena, parola_italiana):
        if parola_aliena not in self.dizionario:
            self.dizionario[parola_aliena] = parola_italiana

    def translate(self, parola_aliena):
        return self.dizionario.get(parola_aliena, '')

    def translateWordWildCard(self):
        pass

