jewelry = {'Браслет': ['Золото', 375, 5], 'Кольцо': ['Серебро', 350, 21], 'Цепочка': ['Белое золото', 1278, 2], 'Серёжки': ['Платина', 976, 6]}

def display_menu():
    print("Меню:")
    print("1. Просмотреть описание")
    print("2. Просмотр цены")
    print("3. Просмотр количества изделий")
    print("4. Просмотр всей информации об изделиях")
    print("5. Покупка")
    print("6. До свидания")

display_menu()

while True:
    choice = input("Выберите вариант (1-6): ")

    if choice == "1":
        print("Вы выбрали Вариант 1")
        for item, values in jewelry.items():
            description = values[0]
            print(f"{item}: {description}")

    elif choice == "2":
        print("Вы выбрали Вариант 2")
        for item, values in jewelry.items():
            price = values[1]
            print(f"{item}: {price} руб.")

    elif choice == "3":
        print("Вы выбрали Вариант 3")
        for item, values in jewelry.items():
            quantity = values[2]
            print(f"{item}: {quantity} шт.")

    elif choice == "4":
        print("Вы выбрали Вариант 4")
        for item, values in jewelry.items():
            description = values[0]
            price = values[1]
            quantity = values[2]
            print(f"{item}: {description}, {price} руб., {quantity} шт.")

    elif choice == "5":
        print("Вы выбрали Вариант 5")
        item = input("Введите название изделия: ")
        if item in jewelry:
            values = jewelry[item]
            while True:
                num = input("Введите количество изделий, которое хотите приобрести: ")
                num = int(num)
                if num <= values[2]:
                    sum = num * values[1]
                    kol = values[2] - num
                    print(f"Сумма к оплате: {sum}")
                    print(f"Оставшееся количество изделий: {kol}")
                    break
                else:
                    print("Недостаточное количество изделий.")
                    choice = input("Хотите попробовать ещё раз? (Да/Нет): ")
                    if choice.lower() == "нет":
                        print("Выход из раздела покупки.")
                        break

    elif choice == "6":
        print("Вы выбрали выход. До свидания!")
        break
    else:
        print("Некорректный вариант. Пожалуйста, выберите снова.")