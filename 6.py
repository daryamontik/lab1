numbers = (170, 2, -3440, 5, 40, 648)

sum = 0
for num in numbers:
    if num < 0:
        break
    sum += num

print("Сумма элементов до первого отрицательного:", sum)