import json
books = [ "genesis", "exodo", "levitico", "numeros", "deuteronomio", "josue", "jueces", "rut", "i-samuel", "ii-samuel", "i-reyes", "ii-reyes", "i-cronicas", "ii-cronicas", "esdras", "nehemias", "tobias", "judit", "ester", "job", "salmos", "i-macabeos", "ii-macabeos", "proverbios", "eclesiastes", "cantar", "sabiduria", "eclesiastico", "isaias", "jeremias", "lamentaciones", "baruc", "ezequiel", "daniel", "oseas", "joel", "amos", "abdias", "jonas", "miqueas", "nahun", "habacuc", "sofonias", "ageo", "zacarias", "malaquias", "mateo", "marcos", "lucas", "juan", "hechos", "romanos", "i-corintios", "ii-corintios", "galatas", "efesios", "filipenses", "colosenses", "i-tesalonicenses", "ii-tesalonicenses", "i-timoteo", "ii-timoteo", "tito", "filemon", "hebreos", "santiago", "i-pedro", "ii-pedro", "i-juan", "ii-juan", "iii-juan", "judas", "apocalipsis" ]

x = [{'id':num+1, 'name': book} for (num, book) in enumerate(books)]

with open('bookList.json', 'w') as outfile:
    json.dump(x, outfile)

print (x)