from inventory_report.reports.simple_report import SimpleReport


class CompleteReport():
    @classmethod
    def generate(cls, lista_test):
        report = SimpleReport.generate(lista_test)
        return (
            f"{report}\n"
            f"{cls.report_quantity_stock_by_company(lista_test)}"
        )

    @classmethod
    def report_quantity_stock_by_company(cls, entry_list):
        return_list = []
        contador = 0
        list_cia = []
        string_return = ""
        for iten in entry_list:
            list_cia.append(iten["nome_da_empresa"])

        for ite in entry_list:
            if not ite["nome_da_empresa"] in return_list:
                contador = list_cia.count(ite["nome_da_empresa"])
                return_list.append(ite["nome_da_empresa"])
                string_return += f'- {ite["nome_da_empresa"]}: {contador}\n'
        return (
          f"Produtos estocados por empresa: \n"
          f"{string_return}"
        )


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
    print(CompleteReport.generate(lista_test))
