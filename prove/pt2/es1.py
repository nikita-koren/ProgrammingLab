def ore_minuti (minuti):
    ore = minuti // 60
    print(ore)
    min = minuti - (ore * 60)
    return print('{} minuti, è in realtà {}ore e {}minuti'.format(minuti, ore, min))

ore_minuti(538)