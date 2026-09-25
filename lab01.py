#1
#a = int(input("Введіть число: "))

#if a % 2:
    #print("Число парне")
#else:
    #print("Число не парне")

#2
#age = int(input("Введіть ваш вік: "))

#if age >= 18:
    #print("Ви повнолітні!")
#else:
    #print("Ви повнолітні!")
#3
#r = int(input("Введіть радіус кола: "))
#c = 2 * 3.14 * r
#s = 3.14*r**2

#print("Довжина: ", c, "Площа: ", s)

#4
#a = int(input("Введіть число: "))
#b = int(input("Введіть число: "))
#if a>b:
    #print(a)
#elif b>a:
    #print(b)
#else:
    #print("Числа рівні: ", a, "==", b )
#5
#x,y = int(map(input("Введіть координати точки: ").split()))
#if x > 0 and y > 0:
    #print("1 Чверть")
#elif x < 0 and y > 0:
    #print("2 чверть")
#elif x < 0 and y < 0:
    #print("3 чверть")
#elif x > 0 and y < 0:
    #print("4 чверть")
#else:
    #print("Точка лежить на початку координат, або на осі координат")
#6
#N, k, p1, p2 = map(int, input().split())
#a = (N // k) * p2 + (N % k) * p1
#b = (N // k + 1) * p2
#print(min(a, b))