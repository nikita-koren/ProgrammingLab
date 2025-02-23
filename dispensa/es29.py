parametro = 0
nome_file_parametro = 'test.txt'
try:
    file_parametro = open(nome_file_parametro, 'r')
    parametro_come_stringa = file_parametro.read()
    parametro_come_float = float(parametro_come_stringa)
except IOError:
    print('Non posso leggere il file!')
    print('Userò il vaore di default per il parametro')
except ValueError:
    print('Non posso convertire il parametro a valore numerico!')
    print('Errore di valore, il parametro valeva "{}".')
    print('Userò il valore di default per il parametro')
except Exception as error:
    print('Errore generico: "{}".'.format(error))
    print('Userò il valore di default per il parametro'.format(parametro_come_stringa))
else:
    parametro = parametro_come_float
finally:
    file_parametro.close()