from random import randint

def flip_coin(choice):
    while choice.lower() == '':
        print('Выпал орёл!' if randint(0,1) == 1 else 'Выпала решка!')
        choice = input('Бросить монету?')



decision = input('Бросить монету?')

flip_coin(decision)



count1 = 0
count2 = 0
for _ in range(1000):
    num = randint(0, 1)
    if num == 0:
        # print('Орел')
        count1 += 1
    else:
        # print('Решка')
        count2 += 1
print(f'Орлов выпало: {count1}')
print(f'Решек выпало: {count2}')
print(count1 * 100 / (count2 + count1))