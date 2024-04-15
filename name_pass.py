import random

target= input("enter pass ; ")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


while True:
    number = ''.join(str(random.randint(0, 9)) for _ in range(5))
    letter = ''.join(random.choice(letters) for _ in range(1))
    matched = False
    for _ in range(1):
        
        password = letter + number
        print(password)
        if target == password:
            matched = True
            break
    if matched:
        print('pass match')
        break
else:
    print("not matched ")

