import random

target = 10
for _ in range(99):
    matched = False
    for _ in range(3):
        number = int(''.join(str(random.randint(0, 9)) for _ in range(2)))
        print(number)
        if target == number:
            matched = True
            break
    if matched:
        print('pass match')
        break
else:
    print("not matched after 10 time")
