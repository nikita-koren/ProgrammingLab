
class TrendModel():

    def prevedii(self,mesi):
        for i in mesi:
            print(i)
        return
    
    def prevedi (self, mesi):
        if len(mesi) != 3:
            raise ValueError('Passati {} mesi'.format(len(mesi))) + 'ma il modello richiede di averne 3.'
        #liam
        if len(mesi) < 3:
            raise ValueError("Impossibile calcolare la variazione media: dati insufficienti")
    
        #liam

        variazioni = []
        quantità_precedente = None

        for quantità in mesi:
            if quantità_precedente is not None:
                variazioni.append(quantità - quantità_precedente) #calcolo della differenza
            quantità_precedente = quantità

            print(f"Debug: variazioni calcolate = {variazioni}")  # Debug
            
        variazione_media = (sum(variazioni))/len(variazioni)
        previsto = mesi[-1] + variazione_media
        return previsto
    