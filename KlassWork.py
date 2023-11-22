class Coffee:
    def __init__(self, name, menu = [], order = []):
        self.name = name
        self.menu = menu
        self.order = order

    def make_order(self):
        for i in self.menu:
            if i["name"] == name:
                self.order.append(i)

    def sum(self):
        return sum(i["price"] for i in self.order)

coffee = Coffee("Питон", [{"name": "латте", "price:": 200}, {"name": "американо", "price": 150}, {"name": "раф", "price": 200}])
choice = input(f"Добро пожаловать! Меню: {coffe.menu}\nВ нашем кофе \"{coffe.name}\" вы можете сделать следующее: \n1. сделать заказ\n2.Посчитать итоговую сумму\nВаш выбор: ")
while True:
    match choice:
        case "1":
            name = input("Введите название напитка")
            coffee.make_order(name.lower())
            print(coffee.order)
        case "2":
            pass
        case _:
            print("Такой услуги нет")