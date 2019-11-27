import os, time
from models import Candidato, Bem
from views import CandidatoViewModel, BemViewModel
from DoubleChainList import DoubleChainList


class Controller():
    def __init__(self):
        self.__candidatos = DoubleChainList()
    
    @property
    def candidatos(self):
        return self.__candidatos

    # TODO 1 OK
    def load_candidatos(self, local):
        for filename in os.listdir(local):
            if filename.endswith(".csv"):

                with open(local + filename, 'r') as file:
                    for line in file.readlines()[1:100]:
                        c = CandidatoViewModel.from_csv(line)
                        self.__candidatos.append(c)
    
    # TODO 2 OK
    def load_bens(self, local):
        bens = DoubleChainList()

        for filename in os.listdir(local):
            if filename.endswith(".csv"):

                with open(local + filename, 'r') as file:
                    for line in file.readlines()[1:20]:
                        bem = BemViewModel.from_csv(line)

                        for candidato in self.__candidatos:
                            if candidato.id_candidato == bem.id_candidato:
                                candidato.append_bem(bem)

    # TODO 4 OK
    def show(self, the_list):
        for item in the_list:
            print(str(item))

    # TODO 3 OK
    def search(self, query=lambda x: x != None):
        return DoubleChainList(filter(query, self.__candidatos))
    
    # TODO 5 OK
    def average(self, attribute=""):
        if hasattr(Candidato(), attribute):
            groups = {}

            for candidate in self.__candidatos:
                group = getattr(candidate, attribute)
                total = candidate.total_declarado

                if group not in groups: groups[group] = DoubleChainList([total])
                else: groups[group].append(total)
            
            return {k: sum(v)/len(v) for k, v in a.items()}
        else:
            raise ValueError("Invalide attribute in Candidato()")
    
    # TODO 6 OK
    def remove(self, query=lambda x: x != None):
        self.__candidatos = DoubleChainList(filter(lambda x: not query(x), self.__candidatos))


def main():
    times = {}
    c = Controller()

    start = time.time()
    c.load_candidatos("./data/candidatos/")
    total = time.time() - start
    times["candidatos"] = total

    print(f"> Time to load candidatos: {total}")

    start = time.time()
    c.load_bens("./data/bens/")
    total = time.time() - start
    times["bens"] = total

    print(f"> Time to load bens: {total}")

    start = time.time()
    c.show(c.search(query=lambda x: x.nome_na_urna.lower().startswith("pedro") ))
    total = time.time() - start
    times["query-show"] = total

    print(f"> Time to query and show: {round(total, 4)}")


    with open('./out_time.txt', 'w') as file:
        for k, v in times:
            file.readline(f"[{k}]: {round(v, 4)}s")

if __name__ == "__main__":
    main()