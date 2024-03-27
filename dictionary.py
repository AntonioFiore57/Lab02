#
class Dictionary:
    def __init__(self):
        self.dizionario = dict()


    def addWord(self,parola_aliena, parola_italiana):
        self.dizionario.append(parola_aliena, parola_italiana)
        self.dizionario.sort()



    def translate(self, parola_aliena):
        posizione = self._ricerca_lineare(parola_aliena)
        return self.dizionario[posizione][1] if posizione != -1 else ''


    def translateWordWildCard(self):
        pass

    def _ricerca_lineare(self, parola_aliena):
        trovato = False
        for i in len(self.dizionario):
            if self.dizionario[i][0] == parola_aliena:
                trovato = True
                break
        return i if trovato else -1
