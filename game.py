#Записываем наш первый код "Угадай число"
import numpy as np
number = np.random.randint(1, 101) # загадываем число
#Создаём переменную счётчик, чтобы в дальнейшем посчитать кол-во попыток угадывания
count = 0
#Теперь пишем цикл, который позволит нам создавать и угадывать числа
while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100"))
#predict_number это введенное польз. число. Проверим соответ-т ли введ.польз.число загаданному
    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла