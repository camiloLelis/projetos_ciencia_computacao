class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.__resquestsLanchonete = []
        self.__minInventury = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        self.__replenishStock = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, customer, order, day):
        if self.stockConsultation(order) is False:
            return False
        self.__resquestsLanchonete.append((customer, order, day))
        self.controlStock(order)

    def get_quantities_to_buy(self):
        return self.__replenishStock

    def controlStock(self, order):
        getIngredients = self.INGREDIENTS[order]
        for itens in getIngredients:
            self.__replenishStock[itens] += 1
            self.__minInventury[itens] -= 1

    def stockConsultation(self, order):
        getIngredients = self.INGREDIENTS[order]
        for itens in getIngredients:
            if self.__minInventury[itens] < 1:
                return False

    def get_available_dishes(self):
        return set(self.INGREDIENTS.keys())
