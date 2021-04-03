n = input("input your name: ")
a = int(input("input your age: "))

n = len(n)
n2 = n * 4

if n == a:
    print("Счастливім будеш!")
elif n2 < a:
    print("Ну, Норм.")
else:
    print("Потянет.")
