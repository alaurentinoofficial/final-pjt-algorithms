from models import Candidato, Bem
from views import CandidatoViewModel, BemViewModel
from DoubleChainList import DoubleChainList


class Controle():
    def __init__(self):
        self.__candidatos = DoubleChainList()
    
    @property
    def candidatos(self):
        return self.__candidatos

    def load_candidatos(self):
        with open('./data/candidatos/consulta_cand_2014_BA.csv', 'r') as file:
            for line in file.readlines()[1:20]:
                c = CandidatoViewModel.from_csv(line)
                self.__candidatos.append(c)
    
    def load_bens(self):
        bens = DoubleChainList()

        with open('./data/bens/bem_candidato_2014_BRASIL.csv', 'r') as file:
            for line in file.readlines():
                c = BemViewModel.from_csv(line)
                bens.append(c)

            for c in self.__candidatos:
                c.bens = filter(lambda x: x.id_candidato == c.id_candidato, bens)

    def search(query=lambda x: x != None):
        return filter(query, self.__candidatos)

    def remove(query=lambda x: x != None):
        self.__candidatos = filter(lambda x: not query(x), self.__candidatos)

def main():
    c = Controle()
    c.load_candidatos()
    c.load_bens()

    for candidate in c.candidatos:
        print(str(candidate))

if __name__ == "__main__":
    main()