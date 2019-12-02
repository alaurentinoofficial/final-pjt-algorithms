import time
from list_csv_files import list_csv_from
from Candidato import Candidato
from Bem import Bem
from CandidatoViewModel import CandidatoViewModel
from BemViewModel import BemViewModel
from HashTable import HashTable
from DoubleChainList import DoubleChainList, Ordering


class Controller():
    def __init__(self, orderby=None):
        self.__candidatos = DoubleChainList(orderby=lambda a, b: orderby(a, b) if orderby != None else None)
    
    @property
    def candidatos(self):
        return self.__candidatos

    # TODO 1 OK
    def load_candidatos(self, local):
        for filename in list_csv_from(local):
            with open(local + filename, 'r') as file:
                for line in file.readlines()[1:]:
                    c = CandidatoViewModel.from_csv(line)
                    self.__candidatos.append(c)
    
    # TODO 2 OK
    def load_bens(self, local):
        for filename in list_csv_from(local):
            bens = HashTable()

            with open(local + filename, 'r') as file:
                for line in file.readlines()[1:]:
                    bem = BemViewModel.from_csv(line)

                    if bem.id_candidato in bens:
                        bens[bem.id_candidato].append(bem)
                    else:
                        bens[bem.id_candidato] = DoubleChainList([bem])

            for candidato in self.__candidatos:
                if candidato.id_candidato in bens:
                    candidato.bens = bens[candidato.id_candidato]
            
            del(bens)

    # TODO 4 OK
    @staticmethod
    def show(the_list):
        for item in the_list:
            print(str(item))

    # TODO 3 OK
    def search(self, query=lambda x: x != None):
        return DoubleChainList(filter(query, self.__candidatos))
    
    # TODO 5 OK
    def average(self, attribute=""):
        if hasattr(Candidato(), attribute):
            groups = HashTable()

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

    # With the Ordering compare you can pass the parameters to sort the candidates into a controller
    # asceding = enables the asceding order like {1, 2, 3, 4}, or when disabled {4, 3, 2, 1}
    # key = select the field will be used to sort
    c = Controller(orderby=Ordering.compare(asceding=True, key=lambda x: x.nome_na_urna))

    # Load the candidates
    start = time.time()
    c.load_candidatos("./data/candidatos/")
    total = time.time() - start
    times["candidatos"] = total

    print(f"> Time to load candidatos: {total}")

    # Load the bens
    start = time.time()
    c.load_bens("./data/bens/")
    total = time.time() - start
    times["bens"] = total

    print(f"> Time to load bens: {total}")

    # Makes a query into candidates and print in screen
    # query = lambda which returns a boolean type (True/False)
    start = time.time()
    (Controller.show(
            c.search(query=lambda x: x.nome_na_urna.lower().startswith("a"))))
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