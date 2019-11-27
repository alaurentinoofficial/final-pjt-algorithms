from DoubleChainList import DoubleChainList

class Candidato:
    def __init__(self, ano_eleicao="", uf="", cod_cargo="", descricao_cargo="", nome_candidato="", id_candidato="", numero_na_urna="", cpf="", nome_na_urna="", numero_partido="", nome_partido="", sigla_partido="", cod_ocupacao_candidato="", descricao_ocupacao="", data_nascimento="", sexo="", grau_instrução="", estado_civil="", uf_nascimento="", municipio_nascimento="", situacao_pos_pleito="", situacao_candidatura="", bens=DoubleChainList()):
        self.__ano_eleicao = ano_eleicao # Ano da eleição
        self.__uf = uf # Sigla da UF
        self.__cod_cargo = cod_cargo# Código do Cargo
        self.__descricao_cargo = descricao_cargo # Descrição do cargo
        self.__nome_candidato = nome_candidato # Nome do candidato
        self.__id_candidato = id_candidato # ID do candidato (número sequencial do candidato gerado pelos sistemas eleitorais)
        self.__numero_na_urna = numero_na_urna # Número na urna
        self.__cpf = cpf # CPF
        self.__nome_na_urna = nome_na_urna # Nome na urna
        self.__numero_partido = numero_partido # Número do partido
        self.__nome_partido = nome_partido # Nome do partido
        self.__sigla_partido = sigla_partido # Sigla do partido
        self.__cod_ocupacao_candidato = cod_ocupacao_candidato # Código de ocupação do candidato
        self.__descricao_ocupacao = descricao_ocupacao # Descrição da ocupação
        self.__data_nascimento = data_nascimento # Data de nascimento (armazenada como dia, mês e ano)
        self.__sexo = sexo # Sexo do candidato
        self.__grau_instrução = grau_instrução # Grau de instrução
        self.__estado_civil = estado_civil # Estado civil
        self.__uf_nascimento = uf_nascimento # UF nascimento
        self.__municipio_nascimento = municipio_nascimento # Nome do município de nascimento
        self.__situacao_pos_pleito = situacao_pos_pleito # Situação do candidato pós pleito (eleito, não eleito, suplente)
        self.__situacao_candidatura = situacao_candidatura # Situação da candidatura (deferida ou indeferida)
        self.__bens = bens # Lista de bens (objetos a serem detalhados a seguir)
    
    def __str__(self):
        out = f"""
        {self.__nome_na_urna} -- {self.__numero_na_urna} -- {self.__sigla_partido}
        {self.__descricao_cargo} ({self.__uf}) | {self.__municipio_nascimento} ({self.__uf_nascimento})
        
        Resumo dos bens:
        \t- Total declarado: {sum([bem.valor for bem in self.__bens])}
        \t- Total por tipo de bem:\n
        """

        tipo_bens = {}

        for i in range(self.__bens.length):
            bem = self.__bens[i]
            tipo_bens[bem.desc_tipo] = bem.valor + (0 if bem.desc_tipo not in tipo_bens else tipo_bens[bem.desc_tipo])

        for tipo, valor in tipo_bens.items():
            out += f"\t\t- {tipo}: R$ {valor}"

        return out
    
    def __repr__(self):
        return self.__str__()
    
    def __lt__(self, item):
        if isinstance(item, Candidato):
            return self.__nome_candidato < item.__nome_candidato
        elif type(item) == str:
            return self.__nome_candidato < item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __le__(self, item):
        if isinstance(item, Candidato):
            return self.__nome_candidato <= item.__nome_candidato
        elif type(item) == str:
            return self.__nome_candidato <= item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __gt__(self, item):
        if isinstance(item, Candidato):
            return self.__nome_candidato  > item.__nome_candidato
        elif type(item) == str:
            return self.__nome_candidato > item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __ge__(self, item):
        if isinstance(item, Candidato):
            return self.__nome_candidato  >= item.__nome_candidato
        elif type(item) == str:
            return self.__nome_candidato >= item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __eq__(self, item):
        if isinstance(item, Candidato):
            return self.__nome_candidato == item.__nome_candidato and self.__cpf  >= item.__cpf
        elif type(item) == str:
            return self.__nome_candidato == item
    
    def __ne__(self, item):
        if isinstance(item, Candidato):
            return self.__nome_candidato != item.__nome_candidato or self.__cpf  != item.__cpf
        else:
            return self.__nome_candidato != item

    @property
    def total_declarado(self):
        return sum([bem.valor for bem in self.__bens])

    @property
    def bens(self):
        return self.__bens

    @property
    def bens_str(self):
        return "\n".join([str(bem) for bem in self.__bens])

    # @bens.setter
    # def bens(self, x):
    #     if isinstance(x, DoubleChainList):
    #         self.__bens = x

    def append_bem(self, x):
        self.__bens.append(x)
    
    @property
    def nome_partido(self):
        return self.__nome_partido

    @nome_partido.setter
    def nome_partido(self, x):
        self.__nome_partido = x


    @property
    def cod_cargo(self):
        return self.__cod_cargo

    @cod_cargo.setter
    def cod_cargo(self, x):
        self.__cod_cargo = x


    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, x):
        self.__cpf = x


    @property
    def cod_ocupacao_candidato(self):
        return self.__cod_ocupacao_candidato

    @cod_ocupacao_candidato.setter
    def cod_ocupacao_candidato(self, x):
        self.__cod_ocupacao_candidato = x


    @property
    def descricao_ocupacao(self):
        return self.__descricao_ocupacao

    @descricao_ocupacao.setter
    def descricao_ocupacao(self, x):
        self.__descricao_ocupacao = x


    @property
    def ano_eleicao(self):
        return self.__ano_eleicao

    @ano_eleicao.setter
    def ano_eleicao(self, x):
        self.__ano_eleicao = x


    @property
    def situacao_candidatura(self):
        return self.__situacao_candidatura

    @situacao_candidatura.setter
    def situacao_candidatura(self, x):
        self.__situacao_candidatura = x


    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, x):
        self.__sexo = x


    @property
    def sigla_partido(self):
        return self.__sigla_partido

    @sigla_partido.setter
    def sigla_partido(self, x):
        self.__sigla_partido = x


    @property
    def id_candidato(self):
        return self.__id_candidato

    @id_candidato.setter
    def id_candidato(self, x):
        self.__id_candidato = x


    @property
    def nome_candidato(self):
        return self.__nome_candidato

    @nome_candidato.setter
    def nome_candidato(self, x):
        self.__nome_candidato = x


    @property
    def nome_na_urna(self):
        return self.__nome_na_urna

    @nome_na_urna.setter
    def nome_na_urna(self, x):
        self.__nome_na_urna = x


    @property
    def numero_na_urna(self):
        return self.__numero_na_urna

    @numero_na_urna.setter
    def numero_na_urna(self, x):
        self.__numero_na_urna = x


    @property
    def situacao_pos_pleito(self):
        return self.__situacao_pos_pleito

    @situacao_pos_pleito.setter
    def situacao_pos_pleito(self, x):
        self.__situacao_pos_pleito = x


    @property
    def estado_civil(self):
        return self.__estado_civil

    @estado_civil.setter
    def estado_civil(self, x):
        self.__estado_civil = x

    @property
    def grau_instrução(self):
        return self.__grau_instrução

    @grau_instrução.setter
    def grau_instrução(self, x):
        self.__grau_instrução = x


    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, x):
        self.__data_nascimento = x


    @property
    def descricao_cargo(self):
        return self.__descricao_cargo

    @descricao_cargo.setter
    def descricao_cargo(self, x):
        self.__descricao_cargo = x


    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, x):
        self.__uf = x


    @property
    def numero_partido(self):
        return self.__numero_partido

    @numero_partido.setter
    def numero_partido(self, x):
        self.__numero_partido = x


    @property
    def uf_nascimento(self):
        return self.__uf_nascimento

    @uf_nascimento.setter
    def uf_nascimento(self, x):
        self.__uf_nascimento = x


    @property
    def municipio_nascimento(self):
        return self.__municipio_nascimento

    @municipio_nascimento.setter
    def municipio_nascimento(self, x):
        self.__municipio_nascimento = x