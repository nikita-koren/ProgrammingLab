my_file = open('shampoo_sales.txt', 'r')
# Leggo il contenuto
my_file_contents = my_file.read()
# Stampo a schermo i primi 50 caratteri
if len(my_file_contents) > 50:
    print(my_file_contents[0:50] + '...')
else:
    print(my_file_contents)

for line in my_file:
    print(line)
# Chiudo il file
my_file.close()

my_file = open('shampoo_sales.txt', 'r')
my_file_contents = my_file.read()
print(my_file_contents)
my_file.close()

my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    print(line)
my_file.close()