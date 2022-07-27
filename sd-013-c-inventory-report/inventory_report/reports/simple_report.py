import statistics
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, dict_list):
        return (
            f"Data de fabricação mais antiga: "
            f"{cls.get_older_date_fab(dict_list)}\n"
            f"Data de validade mais próxima: "
            f"{cls.get_closer_date_valid(dict_list)}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{cls.get_larger_stock_cia(dict_list)}\n"
        )

    @classmethod
    def get_older_date_fab(cls, dict_list):
        myArray = []
        for item in dict_list:
            myArray.append(item["data_de_fabricacao"])
        return min(myArray)

    @classmethod
    def get_closer_date_valid(cls, dict_list):
        today = datetime.today()
        myArray = []
        for item in dict_list:
            if datetime.strptime(item["data_de_validade"], "%Y-%m-%d") > today:
                myArray.append(item["data_de_validade"])
        return min(myArray)

    @classmethod
    def get_larger_stock_cia(cls, dict_list):
        data_set = []
        for item in dict_list:
            data_set.append(item["nome_da_empresa"])
        return statistics.mode(data_set)


if __name__ == "__main__":
    lista_test = [
        {
            "id": 1,
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim",
        },
        {
            "id": 2,
            "nome_do_produto": "sodium ferric gluconate complex",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2020-05-31",
            "data_de_validade": "2023-01-17",
            "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
            "instrucoes_de_armazenamento": "duis bibendum morbi",
        },
        {
            "id": 3,
            "nome_do_produto": "Dexamethasone Sodium Phosphate",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2019-09-13",
            "data_de_validade": "2023-02-13",
            "numero_de_serie": "BA52 2034 8595 7904 7131",
            "instrucoes_de_armazenamento": "morbi quis tortor id",
        },
        {
            "id": 4,
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories, Inc.",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]
    print(SimpleReport.generate(lista_test))
