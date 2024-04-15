import random

target = 1021
num = ''.join(str(random.randint(1, 9)) for _ in range(4))
for _ in range(10000000):
    matched = False
    for _ in range(3):
        number = int(num)
        if target == number:
            matched = True
            print(number)
            break
    if matched:
        print('pass match')
        break
else:
    print("not matched after 10 time")
