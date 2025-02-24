my_file2 = open('saluti.txt', 'w')
my_file2.write('Ciao mondo!\n')
my_file2.close()

my_file = open('saluti.txt', 'a')
my_file.write('Addio!\n')
my_file.close()

with open('saluti.txt', 'a') as file:
    file.write('A mai più :)')

