class Storage():
    def __init__(self, size=25):
        """
        происходит инициализация
        param size:размер таблицы
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def __str__(self):
        """
        возвращет хранилище в виде строки
        """
        output = ""
        for i in range(self.size):
            if (self.table[i]):
                output += f"\n{i}: {self.table[i]}"
        return output

    def hashing(self, key):
        """
        хэширование ключа для этой таблицы 
        param key: ключ
        return: захэшированное значение ключа(индекс в таблице)
        """
        try:
            hash(key)
            return hash(key) % self.size
        except TypeError as e:
            print(f"этот тип данных не поддерживает хэширование {e}")

    def put(self, key, value):
        """
        Вставляет пару ключ-значение в хэш-таблицу.
        :param key: Ключ.
        :param value: Значение.
        """
        index = self.hashing(key)
        for i in self.table[index]:
            if i[0] == key:
                i[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        """
        получаем значение по ключу
        param key: ключ
        """
        index = self.hashing(key)
        for i in self.table[index]:
            if i[0] == key:
                return i[1]
        print("такого элемента в таблице не найдено...")
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def delete(self, key):
        """
        удаляет пару ключ значение
        param key: ключ
        """
        index = self.hashing(key)
        for ind, i in enumerate(self.table[index]):
            if i[0] == key:
                del self.table[index][ind]
                return
            
    def clear(self):
        """
        чистит все хранилище
        """
        for i in range(self.size):
            if (self.table[i]):
                self.table[i]=[]


if __name__ == "__main__":
    # sx=[1,2]
    test = Storage()
    test.put("apple", 10)
    test.put("banana", 20)
    test.put("orange", 30)
    test.put(12, "orange")
    # test.put(sx,12)
    test[44] = 11
    test[22.1]= (1+2==3)
    test[1+2==3]=22.1
    print(test.get(True))

    print(test.get("apple"))
    print(test.get("banana"))
    print(test.get("orange"))
    print(test.get(12))
    print(test)
    print(test[12])
    test.delete("banana")
    test.clear()
    print(test)
    print(test.get("nbas"))
    print(test.get("bandana"))
