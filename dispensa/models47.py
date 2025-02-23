class Model():

    def fit(self, data):
        #fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
    
    def predict(self, data):
         #fit non implementato nella classe base
         raise NotImplementedError('Metodo non implementato')
    
    def evaluate (self, data):
        #Setto l'indice di cutoff per dividere i dati nel 70% di fit e 30% di test
        fit_data_70 = int(len(data) * 0.7)

        #Divido i dati
        fit_data = data[:fit_data_70]
        test_data = data[fit_data_70:]
        
        #provo a fare il fit del modello e nel caso non sia supportato passo
        try:
            self.fit(fit_data)
        except Exception as exc:
            if isinstance (exc, NotImplementedError):
                pass
        else:
            raise Exception('Il medoto fit è implementato ma ha sollevato una eccezione: {}'. format(exc))
        
        # Far fare al modello le previsioni sul
        # # test set e confrontarle con i dati veri,
        # # calcolando il MAE (evaluation_mae) è
        # # invece lasciato al lettore
        evaluation_mae = None
        
        # Torno il risultato della valutazione
        return evaluation_mae


class TrendModel():

    def __init__(self, window = 3):
        self.window = window
    
    def validate_data(self, data):
        if len(data) != self.window:
            raise ValueError('Passati {} mesi, ma il modello richiede di averne {}.'.format(len(data), self.window))
        
    def calcola_variazione_media(self, data):
        variazioni = [data[i] - data[i - 1] for i in range(1, len(data))]
        print(variazioni)
        return sum(variazioni) / len(variazioni)

    def predict(self, data):
        self.validate_data(data)
        prediction = data[-1] + self.calcola_variazione_media(data)
        return prediction
    
    def evaluate(self, data):
        cutoff = int(len(data) * 0.7)

        fit_data = data[:cutoff]
        test_data = data[cutoff:]

        if len(fit_data) < self.window or len(test_data) == 0:
            raise ValueError("Dati insufficienti per la valutazione")

        predictions = []
        actual_values = []
        
        for i in range(self.window, len(data)):  
            window_data = data[i - self.window:i]
            try:
                pred = self.predict(window_data)
                predictions.append(pred)
                actual_values.append(data[i])
            except ValueError:
                continue  

         # STAMPA I DATI PER IL DEBUG
        print("\nValori reali:", actual_values)
        print("Previsioni  :", predictions)

        
        errors = [abs(predictions[i] - actual_values[i]) for i in range(len(predictions))]
        print("Errori assoluti:", errors)
        evaluation_mae = sum(errors) / len(errors) if errors else None
        print("MAE calcolato:", evaluation_mae)

        return evaluation_mae
    

class FitTrendModel(TrendModel):

    def __init__(self, data):
        self.variazione_media_storica = self.calcola_variazione_media(data) 
    
    def predict (self, data):
        try:
            self.variazione_media_storica
        except AttributeError:
            raise Exception('Il modello non è fittato!')
        self.validate_data(data)

        prediction = data[-1] + (self.variazione_media_storica + self.calcola_variazione_media(data))/2
        return prediction