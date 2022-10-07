#4
# number = int(input('number = '))
# a = number // 100
# b = number // 10 % 10
# c = number % 10
# print(a * b * c)


#5
# while(1):
#     a = int(input('a='))
#     b = int(input('b='))
#     n = a * b
#     while a != 0 and b != 0:
#         if a>b:
#             a %= b
#         else:
#             b %= a
#     ekub = a + b
#     ekuk = n//ekub
#     print(ekub,ekuk)


#Fibonachi
# n = int(input("n = "))
# n1, n2 = 0, 1
# count = 0
# if n <= 0:
#    print("musbat son kiriting")
# elif n == 1:
#    print("Fibonachi son qatori",n,":")
#    print(n1)
#
# else:
#    print("Fibonachi qatori:")
#    while count < n:
#        print(n1)
#        last = n1 + n2
#        n1 = n2
#        n2 = last
#        count += 1

n = float(input('n = '))
m = float(input('m = '))
if n % m == 0:
    print(int(n//m))
# elif n % m != 0:
#     print(n,'/','m')
else:
    b = n//m
    c = n-b*m

    print(b,c,'/',m)