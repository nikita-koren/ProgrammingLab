from models import TrendModel

test_data = [50, 52, 60]
trend_model = TrendModel()

# Applico il modello
prevedi = trend_model.prevedi(test_data)

print(prevedi)

# Testo che il risultato sia corretto
if prevedi != 65:
    raise Exception('Il modello sbaglia la prediction: ha dato {} invece di 65'.format(prevedi))

# Testo anche che il modello non possa funzionare su un numero errato di mesi
wrong_test_data = [50, 52, 60, 70]

try:
    trend_model.prevedi(wrong_test_data)
except ValueError:
    pass
else:
    raise Exception('Il modello non alza alcuna eccezione se applicato su un numero di mesi diverso da 3')

print('ALL TESTS PASS')