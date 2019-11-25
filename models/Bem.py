

class Bem:
    def __init__(self, id_candidato="", cod_tipo="", desc_tipo="", desc_detalhada="", valor=0):
        self.__id_candidato = id_candidato
        self.__cod_tipo = cod_tipo # Código do tipo de bem
        self.__desc_tipo = desc_tipo # Descrição do tipo de bem
        self.__desc_detalhada = desc_detalhada # Descrição detalhada do bem
        self.__valor = valor # Valor do bem
    
    def __str__(self):
        out = f"""
        {self.__cod_tipo} -- {self.__desc_tipo} -- {self.__id_candidato} -- {self.__valor} Descrição: {self.__desc_detalhada[:80]}
        """

        return out
    
    def __repr__(self):
        return self.__str__()
    
    def __lt__(self, item):
        if isinstance(item, Bem):
            return ((self.__valor, self.__cod_tipo, self.__desc_detalhada) < (item.__valor, item.__cod_tipo, item.__desc_detalhada))
        elif type(item) == int:
            return self.__valor < item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __le__(self, item):
        if isinstance(item, Bem):
            return ((self.__valor, self.__cod_tipo, self.__desc_detalhada) <= (item.__valor, item.__cod_tipo, item.__desc_detalhada))
        elif type(item) == int:
            return self.__valor <= item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __gt__(self, item):
        if isinstance(item, Bem):
            return ((self.__valor, self.__cod_tipo, self.__desc_detalhada) > (item.__valor, item.__cod_tipo, item.__desc_detalhada))
        elif type(item) == int:
            return self.__valor > item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __ge__(self, item):
        if isinstance(item, Bem):
            return ((self.__valor, self.__cod_tipo, self.__desc_detalhada) >= (item.__valor, item.__cod_tipo, item.__desc_detalhada))
        elif type(item) == int:
            return self.__valor >= item
        else:
            raise ValueError("Invalid type comparation!")
    
    def __eq__(self, item):
        if isinstance(item, Bem):
            return self.__valor == item.__valor and self.__desc_detalhada == item.__desc_detalhada
        elif type(item) == int:
            return self.__valor == item
    
    def __ne__(self, item):
        if isinstance(item, Bem):
            return self.__valor != item.__valor or self.__desc_detalhada != item.__desc_detalhada
        else:
            return self.__valor != item
    
    @property
    def id_candidato(self):
        return self.__id_candidato

    @id_candidato.setter
    def id_candidato(self, x):
        self.__id_candidato = x

    @property
    def desc_tipo(self):
        return self.__desc_tipo

    @desc_tipo.setter
    def desc_tipo(self, x):
        self.__desc_tipo = x


    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, x):
        self.__valor = x


    @property
    def cod_tipo(self):
        return self.__cod_tipo

    @cod_tipo.setter
    def cod_tipo(self, x):
        self.__cod_tipo = x


    @property
    def desc_detalhada(self):
        return self.__desc_detalhada

    @desc_detalhada.setter
    def desc_detalhada(self, x):
        self.__desc_detalhada = x