x = int(input("Please eneter the value of 'x': "))

if x < 0:
    print("x is negative number")
elif x < 10 > 0:
    print("x is positive number")
elif x == 0:
    print('x is equal to zero')
elif x < 20 > 10:
    print('x larger then 10 but less then 20')
# elif x > 20:
#     print('x larger then 20')
else:
    print("not defined")

"""if True:  # dead code
    print('Passed')
else:
    print('Failed')"""

if 10 > 5:
    print("Hi")

a = 100
b = 200
c = 300

if a > b and a > c:
    print('a is highest')
elif b > c:
    print('b is highest')
else:
    print('c is greatest')

total = int(input('Enter the total value: '))
if total < 100:
    total = total + 20
elif 100 <= total <= 500:
    total = total + 50
else:
    total = total + 100
print(total)
print("total="+str(total))  # str method
print(f"total={total}")  # f string
