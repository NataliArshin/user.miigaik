# Вариант 16. Посчитать количество выживших женщин по каждому классу обслуживания
with open("data.csv") as file:
    first_class_survived = 0
    second_class_survived = 0
    third_class_survived = 0

    next(file)

    for line in file:
        parts = line.strip().split(',')

        if parts[5] == 'female' and parts[1] == '1':
            if parts[2] == '1':
                first_class_survived += 1
            elif parts[2] == '2':
                second_class_survived += 1
            elif parts[2] == '3':
                third_class_survived += 1

print("Первый класс:", first_class_survived)
print("Второй класс:", second_class_survived)
print("Третий класс:", third_class_survived)