hours = int(input("Введіть кількість годин: "))
if 0 <= hours < 6:
    print("Good Night")
elif 6 <= hours < 13:
    print("Good Morning")
elif 13 <= hours < 17:
    print("Good Day")
elif 17 <= hours < 24:
    print("Good Evening")
else:
    print("Некоректний ввід годин. Введіть число від 0 до 23.")