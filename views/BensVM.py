from ..models.Bem import Bem

class BensViewModel:
    @staticmethod
    def from_csv(line):
        attrs = line.replace('"', "").split(';')

        maps = {
            "cod_tipo": 13,
            "desc_tipo": 14,
            "desc_detalhada": 15,
            "valor": 16
        }

        out = Bem()

        for attr, csv_pos in maps.items():
            setattr(out, attr, attrs[csv_pos])
        
        return out