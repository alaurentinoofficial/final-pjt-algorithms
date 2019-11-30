from Bem import Bem

class BemViewModel:
    @staticmethod
    def from_csv(line):
        attrs = line.replace('"', "").split(';')

        maps = {
            "id_candidato": 11,
            "cod_tipo": 13,
            "desc_tipo": 14,
            "desc_detalhada": 15,
            "valor": 16
        }

        out = Bem()

        for attr, csv_pos in maps.items():
            value = attrs[csv_pos] if attr != "valor" else float(attrs[csv_pos].replace(',', '.'))
            setattr(out, attr, value)

        return out