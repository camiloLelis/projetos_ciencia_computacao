class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        resultFirst = self._data[0]
        del self._data[0]
        return resultFirst

    def search(self, index):
        """Aqui irá sua implementação"""
        if 0 <= index < len(self):
            return self._data[index]
        else:
            raise IndexError("Index out of range")
