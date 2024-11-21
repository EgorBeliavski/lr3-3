mouth=int(input("Введите месяц "))
day = int(input("Введите день "))
if mouth>=3 and mouth<=5:
    print("Весна")
elif mouth>=6 and mouth<=8:
    print("Лето")
elif mouth>=9 and mouth<=11:
    print("Осень")
else:
    print("Зима")