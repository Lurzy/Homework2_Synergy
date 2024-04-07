print("Введите пятизначное целое число: ")
userNumber = int(input())

# Парсю числа на делит целое число на элементы
tensThousands = userNumber // 10000
thousands = (userNumber % 10000) // 1000
hundreds = (userNumber % 1000) // 100
tens = (userNumber % 100) // 10
units = (userNumber % 10)

#Разделил по шагам, чтобы каши не было, в этом шаге возвожу десятки в степень единиц, затем умножает на сотни
constrTensUnits = (tens**units)*hundreds

#Далее считаю разность между tensThousands и thousands
difference = tensThousands - thousands

#Получаю финальный результат, деля constrTensUnits на difference
finalResult = constrTensUnits / difference
print("Результат: ", finalResult)
