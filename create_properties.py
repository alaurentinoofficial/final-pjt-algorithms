get_set = lambda x: ("""
@property
def {0}(self):
    return self.__{0}

@{0}.setter
def {0}(self, x):
    self.__{0} = x
""").format(x)


def write_propeties(properties, output="out.txt", encoding='utf8'):
    out = ""

    for p in properties:
        out += "\n"
        out += get_set(p)

    with open(output, 'w', encoding=encoding) as file:
        file.write(out)


if __name__ == "__main__":   
    target_candidato = {
        "ano_eleicao",
        "uf",
        "cod_cargo",
        "descricao_cargo",
        "nome_candidato",
        "id_candidato",
        "numero_na_urna",
        "cpf",
        "nome_na_urna",
        "numero_partido",
        "nome_partido",
        "sigla_partido",
        "cod_ocupacao_candidato",
        "descricao_ocupacao",
        "data_nascimento",
        "sexo",
        "grau_instrução",
        "estado_civil",
        "uf_nascimento",
        "municipio_nascimento",
        "situacao_pos_pleito",
        "situacao_candidatura",
        "bens"
    }

    target_bem = {
        "cod_tipo",
        "desc_tipo",
        "desc_detalhada",
        "valor"
    }

    write_propeties(target_candidato, output="out_candidato.txt")
    write_propeties(target_bem, output="out_bem.txt")