import time
from utils import list_csv_from
from models import Candidato, Bem
from views import CandidatoViewModel, BemViewModel
from DoubleChainList import DoubleChainList, Ordering


class Controller():
    def __init__(self, orderby=lambda a, b: Ordering.compare(a, b, asceding=True, key=lambda x: x)):
        self.__candidatos = DoubleChainList(orderby=orderby)
    
    @property
    def candidatos(self):
        return self.__candidatos

    # TODO 1 OK
    def load_candidatos(self, local):
        for filename in list_csv_from(local):
            with open(local + filename, 'r') as file:
                for line in file.readlines()[1:20]:
                    c = CandidatoViewModel.from_csv(line)
                    self.__candidatos.append(c)
    
    # TODO 2 OK
    def load_bens(self, local):
        bens = DoubleChainList()

        for filename in list_csv_from(local):
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
    c = Controller(orderby=lambda a, b: Ordering.compare(a, b, asceding=False, key=lambda x: x.nome_na_urna))

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
    times["query-and-show"] = total

    print(f"> Time to query and show: {round(total, 4)}")


    with open('./out_time.txt', 'w') as file:
        out = ""
        
        for k, v in times.items():
            out += f"[{k}]: {round(v, 4)}s\n"
        
        file.write(out)

if __name__ == "__main__":
    main()