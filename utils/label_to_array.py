
with open('./data/candidatos/consulta_cand_2014_BRASIL.csv', 'r') as file:
    for item in enumerate(file.readline().split(";")):
        print(item)

print()

with open('./data/bens/bem_candidato_2014_BRASIL.csv', 'r') as file:
    for item in enumerate(file.readline().split(";")):
        print(item)