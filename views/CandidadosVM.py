from ..models.Candidato import Candidato

class CandidatoViewModel:
    @staticmethod
    def from_csv(line):
        attrs = line.replace('"', "").split(';')

        maps = {
            "ano_eleicao": 2,
            "uf": 10,
            "cod_cargo": 13,
            "descricao_cargo": 14,
            "nome_candidato": 17,
            "id_candidato": 15,
            "numero_na_urna": 16,
            "cpf": 20,
            "nome_na_urna": 18,
            "numero_partido": 27,
            "nome_partido": 29,
            "sigla_partido": 28,
            "cod_ocupacao_candidato": 49,
            "descricao_ocupacao": 50,
            "data_nascimento": 38,
            "sexo": 42,
            "grau_instrução": 44,
            "estado_civil": 46,
            "uf_nascimento": 35,
            "municipio_nascimento": 37,
            "situacao_pos_pleito": 53,
            "situacao_candidatura": 56 # ?
        }

        out = Candidato()

        for attr, csv_pos in maps.items():
            setattr(out, attr, attrs[csv_pos])
        
        return out