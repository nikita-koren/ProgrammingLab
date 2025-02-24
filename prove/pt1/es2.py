# Contare quante volte una lettera è contenuta in una parola
def conta(parola, lettera):
    contatore = 0
    for char in parola: 
        if char == lettera:
            contatore += 1
    return contatore

print(conta("pretererintenzionale", "e"))  