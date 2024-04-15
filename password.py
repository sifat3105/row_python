import random

target = 90
while True:
    matched = False
    for _ in range(7):
        number = int(''.join(str(random.randint(0, 9)) for _ in range(2)))
        print(number)
        if target == number:
            matched = True
            break
    if matched:
        print('pass match')
        break
else:
    print("not matchede")
