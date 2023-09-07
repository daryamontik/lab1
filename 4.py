trees = {'Дуб': 1, 'Сосна': 2, 'Берёза': 3}
flowers = {'Тюлбпаны': 4, 'Ромашки': 5, 'Розы': 6, 'Лилии': 7}
herbs = {'Полынь': 8, 'Шалфей': 9, 'Подорожник': 10, 'Клевер': 11}

plants = trees.copy()
plants.update(flowers)
plants.update(herbs)

print(plants)