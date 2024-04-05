#
class Dictionary:
    def __init__(self):
        """
        La chiave del dizionario è la parola aliena;
        il valore è una lista delle parole italiane
        """
        self.dizionario = dict()


    def addWord(self,parola_aliena, parola_italiana):
        """
        Viene aggiunta la parola italiana al dizionario la cui chiave è la parola aliena.
        Se la parola aliena non è presente nelle chiavi la parola italiana è aggiunta
        come una lista di un solo elemento.
        :param parola_aliena: stringa
        :param parola_italiana: stringa
        :return: None
        """
        if parola_aliena not in self.dizionario:
            self.dizionario[parola_aliena] = [parola_italiana]
        else:
            self.dizionario[parola_aliena].append(parola_italiana)

    def translate(self, parola_aliena):
        """

        :param parola_aliena: stringa
        :return: la lista delle parole italiana; lista vuota se parola aliena non è presente
        """
        lista_parole_italiane = self.dizionario.get(parola_aliena, [])
        #parole_italiane = ', '.join(lista_parole_italiane)
        return lista_parole_italiane

    def translateWordWildCard(self, query):
        """
        Si assume che query contenga di sicuro il carattere jolly '?'
        La funzione costruisce un dizionario in cui le chiavi sono le
        parole aliene che soddisfano il pattern
        e i valori la lista delle parole italiane ad esse associate.
        :param query: stringa che rappresenta la parola aliena con il carattere jolly '?'
        :return: diz_match Dizionario --> chiave: parola aliena: lista parole italiane
        """
        diz_match = dict()
        posizione = query.find('?')
        inizio = query[:posizione]
        fine = query[posizione + 1:]
        for parola_aliena in self.dizionario:
            if parola_aliena.startswith(inizio) and parola_aliena.endswith(fine):
                diz_match[parola_aliena] = self.dizionario[parola_aliena]

        return diz_match

