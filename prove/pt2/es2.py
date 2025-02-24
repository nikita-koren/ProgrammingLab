#Definire una funzione che prende come argomento una parola e una lettera. Ritorna quante volte
# quella lettera è contenuta nella parola.

def conta_lettera (parola, lettera):
    conta = 0
    for i in parola:
        if (i == lettera):
            conta += 1
    return conta

parola = 'supercalifragilisticespiralidoso'
lettera = 'i'
print('nella parola: "{}", la lettera: "{}" è contenuta [{}]volte'.format(parola, lettera, conta_lettera(parola, lettera)))