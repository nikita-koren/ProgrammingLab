mia_var = input()
try:
    mia_var = float(mia_var)
except ValueError:
    print('Non posso convertire "mia_var" a valore numerico!')
    print('Errore di VALORE, "mia_var" valeva "{}".'.format(mia_var))
except TypeError:
    print('Non posso convertire "mia_var" a valore numerico!')
    print('Errore di TIPO, "mia_var" era "{}".'.format(type(mia_var)))
except Exception as error:
    print('Non posso convertire "mia_var" a valore numerico!')
    print('Errore generico: "{}".'.format(error))