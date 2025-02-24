#controllare se è palindromo

def palindromo (lista):
    if lista[::1] == lista[-1::-1]: #0::1 & ::1 stessa cosa
        return True
    else:
        return False
    #bastava return mettere if lista[::1] == lista[-1::-1]

prova1 = "casa"
print(palindromo(prova1))

prova2 = "aerea"
print(palindromo(prova2))

prova3 = "ancora"
print(palindromo(prova3))
