class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.resquestsLanchonete = []

    def __len__(self):
        return len(self.resquestsLanchonete)

    def add_new_order(self, customer, order, day):
        self.resquestsLanchonete.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        maisPedido = dict()
        for linha in self.resquestsLanchonete:
            if linha[0] == customer:
                if linha[1] in maisPedido:
                    maisPedido[linha[1]] += 1
            else:
                maisPedido[linha[1]] = 1
        return f'{max(maisPedido, key=lambda key: maisPedido[key])}'

    def get_never_ordered_per_customer(self, customer):
        customerOrdered = set()
        allItems = set()
        for linha in self.resquestsLanchonete:
            allItems.add(linha[1])
            if linha[0] == customer:
                customerOrdered.add(linha[1])
        iten = allItems - customerOrdered
        return iten

    def get_days_never_visited_per_customer(self, customer):
        customerDays = set()
        allDays = set()
        for linha in self.resquestsLanchonete:
            allDays.add(linha[2])
            if linha[0] == customer:
                customerDays.add(linha[2])
        iten = allDays - customerDays
        return iten

    def get_busiest_day(self):
        maxMovement = self.sumMovement()
        return max(
            maxMovement, key=maxMovement.get
        )

    def get_least_busy_day(self):
        minMovement = self.sumMovement()
        return min(
            minMovement, key=minMovement.get
        )

    def sumMovement(self):
        sumDays = dict()
        for linha in self.resquestsLanchonete:
            if linha[2] in sumDays:
                sumDays[linha[2]] += 1
            else:
                sumDays[linha[2]] = 1
        return sumDays
