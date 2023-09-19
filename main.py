import math
while True:
    try:
        diameter = float(input("Введіть діаметр кола: "))
        break
    except ValueError as e:
        print('Введіть вірний формат діаметру')

choice = input("Оберіть 'площа' або 'периметр' (введіть '1' або '2'): ")
if choice == '1':
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    print(f"Площа кола з діаметром {diameter} дорівнює {area:.2f} квадратних одиниць.")
elif choice == '2':
    circumference = math.pi * diameter
    print(f"Периметр кола з діаметром {diameter} дорівнює {circumference:.2f} одиниць довжини.")
else:
    print("Неправильний вибір. Будь ласка, введіть 'площа' або 'периметр'.")