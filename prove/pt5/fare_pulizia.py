def prova(nome_file_parametro):
    try:
        file_parametro = open(nome_file_parametro)
        parametro_come_stringa = file_parametro.read()
        parametro_come_float = float(parametro_come_stringa)
    except IOError:
        print('Non posso leggere il file!')
        print('Userò il valore di default per il parametro')
    except ValueError:
        print('Non posso convertire il parametro a valore numerico!')
        print('Errore di valore, il parametro valeva {}'.format(parametro_come_stringa))
        print('Userò il valore di default per il parametro')
    except Exception as error:
        print('Errore generico: "{}"'.format(error))
        print('Userò il valore di default per il parametro')
    else: 
        parametro = parametro_come_float
        return parametro
    finally:
        file_parametro.close()
    
test = 'text.txt'
print(prova(test))