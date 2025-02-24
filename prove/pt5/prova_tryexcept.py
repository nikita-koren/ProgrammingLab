my_var = 'Ciao'

try:
    my_var = float(my_var)
except Exception as e:
    print('Non posso convertire "my_var a valore numerico!')
    print('La variabile "my_var" valeva: {}'.format(my_var))
    print('Ed ho avuto questo errore: {}'.format(e))
    print('Uso il valore di default "0.0" per my_var')
    my_var = 0.0
