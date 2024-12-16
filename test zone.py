class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        aboba = open(self.__file_name, 'r')
        names = aboba.read()
        aboba.close()
        return names


    def add(self, *products):
        aboba = self.get_products()
        for i in products:
            if i.name in aboba:
                print(f"Продукт с названием {i.name} уже есть")
            else:
                obaba = open(self.__file_name, 'a')
                obaba.write(f"\n {i} ")
                obaba.close()


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())