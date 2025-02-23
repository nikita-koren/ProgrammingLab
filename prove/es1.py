#covertire da minuti a ore e minuti
def converti_min(min):
    ore = min // 60 # // divisione intera
    resto = min - (ore * 60)  
    return str(ore) + "h:" + str(resto) + "min"

print(converti_min(538))  # Output: "8h:58min"

#oppure
print("l'equivalente di 538 minuti è {}h:{}min" .format(538 // 60, 538 % 60))