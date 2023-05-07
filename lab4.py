import tkinter as tk

class DeliveryCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор доставки")

        # Створюємо вибір способу доставки
        self.delivery_options = ["Самовивіз", "Доставка зовнішньою службою доставки", "Доставка власною службою доставки"]
        self.delivery_var = tk.StringVar(value=self.delivery_options[0])
        self.delivery_label = tk.Label(master, text="Оберіть спосіб доставки:")
        self.delivery_menu = tk.OptionMenu(master, self.delivery_var, *self.delivery_options)
        self.delivery_label.pack()
        self.delivery_menu.pack()

        # Створюємо вибір відстані
        self.distance_label = tk.Label(master, text="Введіть відстань в км:")
        self.distance_entry = tk.Entry(master)
        self.distance_label.pack()
        self.distance_entry.pack()

        # Створюємо кнопку для розрахунку вартості доставки
        self.calculate_button = tk.Button(master, text="Розрахувати вартість доставки", command=self.calculate_cost)
        self.calculate_button.pack()

        # Створюємо відображення результату
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        # Ініціалізуємо стратегії
        self.strategies = {
            "Самовивіз": PickupStrategy(),
            "Доставка зовнішньою службою доставки": ExternalDeliveryStrategy(),
            "Доставка власною службою доставки": OwnDeliveryStrategy(),
        }

    def calculate_cost(self):
        # Отримуємо вибраний спосіб доставки та відстань
        delivery_type = self.delivery_var.get()
        distance = float(self.distance_entry.get())

        # Отримуємо відповідну стратегію та виконуємо розрахунок
        strategy = self.strategies[delivery_type]
        cost = strategy.calculate_cost(distance)

        # Відображаємо результат
        self.result_label.config(text="Вартість доставки: {:.2f} грн.".format(cost))


class DeliveryStrategy:
    def calculate_cost(self, distance):
        pass

class PickupStrategy(DeliveryStrategy):
    def calculate_cost(self, distance):
        return 0

class ExternalDeliveryStrategy(DeliveryStrategy):
    def calculate_cost(self, distance):
        return distance * 10

class OwnDeliveryStrategy(DeliveryStrategy):
    def calculate_cost(self, distance):
        return distance * 5


root = tk.Tk()
app = DeliveryCalculator(root)
root.mainloop()
