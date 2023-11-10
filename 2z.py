class Rub(object):
    """ Класс для работы с рублями и копейками."""

    def __init__(self, rub=0, kop=0):
        self.rub = rub
        self.kop = kop
        self.normalize()

    def normalize(self):
        self.rub += self.kop // 100
        self.kop = self.kop % 100

    def __str__(self):
        return f"{self.rub}.{self.kop:02d} rub"

    def __lt__(self, other):
        return (self.rub, self.kop) < (other.rub, other.kop)

    def __add__(self, other):
        res = Rub(self.rub + other.rub, self.kop + other.kop)
        res.normalize()
        return res


class Goods(object):
    """ Класс описания товара: название и цена"""

    def __init__(self, name='', rub=0, kop=0):
        self.name = name
        self.price = Rub(rub, kop)


def main():
    goods = []
    while True:
        try:
            line = input("Введите название товара и цену (например, 'Хлеб 50.75'): ").split()
            if not line:
                break
            name = line[0]
            price = line[1]
            rub, kop = map(int, price.split('.'))
            goods.append(Goods(name, rub, kop))
        except IndexError:
            print("Пожалуйста, введите название и цену в указанном формате.")
            continue
        except ValueError:
            print("Пожалуйста, введите цену в виде целого числа и дробной части через точку.")
            continue

    goods.sort(key=lambda x: (x.price.rub, x.price.kop))  # сортировка по цене
    for good in goods:
        print(f"{good.name}: {good.price}")  # вывод информации о товаре

    total_price = sum(good.price.rub * 100 + good.price.kop for good in goods)  # вычисление общей стоимости в копейках
    total_price_rub = total_price // 100
    total_price_kop = total_price % 100
    print(f"Общая стоимость: {total_price_rub}.{total_price_kop:02d} rub")

    # запрашиваем ввод суммы для оплаты
    while True:
        try:
            payment = input("Введите сумму для оплаты (в формате 'рубли.копейки'): ")
            rub, kop = map(int, payment.split('.'))
            payment_amount = Rub(rub, kop)
            break
        except ValueError:
            print("Пожалуйста, введите сумму в верном формате.")
            continue

    change = payment_amount - Rub(total_price_rub, total_price_kop)  # вычисление сдачи
    print(f"Сдача: {change}")


if __name__ == "__main__":
    main()