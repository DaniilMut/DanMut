numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Заменить значение None в списке и вычислить среднее арифметическое
numbers[4] = 0
average = sum(numbers) / len(numbers)

# Заменить пропущенный элемент на среднее арифметическое
for i in range(len(numbers)):
    if numbers[i] is 0:
        numbers[i] = average

print("Измененный список:", numbers)