water = 400
milk = 540
beans = 120
cups = 9
money = 550


def remaining():
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()


def buy():
    global water, milk, beans, cups, money
    coffee = input(
        'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
    if coffee == '1':
        if water >= 250 and beans >= 16 and cups >= 1:
            print('I have enough resources, making you a coffee!')
            water -= 250
            milk -= 0
            beans -= 16
            cups -= 1
            money += 4
        else:
            if water < 250:
                print('Sorry, not enough water!')
            elif beans < 16:
                print('Sorry, not enough bean!')
            elif cups < 1:
                print('Sorry, not enough cup!')
    elif coffee == '2':
        if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
            print('I have enough resources, making you a coffee!')
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
            money += 7
        else:
            if water < 350:
                print('Sorry, not enough water!')
            elif beans < 20:
                print('Sorry, not enough bean!')
            elif milk < 75:
                print('Sorry, not enough milk!')
            elif cups < 1:
                print('Sorry, not enough cup!')
    elif coffee == '3':
        if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
            print('I have enough resources, making you a coffee!')
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            money += 6
        else:
            if water < 200:
                print('Sorry, not enough water!')
            elif beans < 12:
                print('Sorry, not enough bean!')
            elif milk < 100:
                print('Sorry, not enough milk!')
            elif cups < 1:
                print('Sorry, not enough cup!')
    print()


def fill():
    global water, milk, beans, cups
    water += int(input('Write how many ml of water do you want to add:\n'))
    milk += int(input('Write how many ml of milk do you want to add:\n'))
    beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
    cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))
    print()


def take():
    global money
    print(f'I gave you ${money}')
    money -= money
    print()


while True:
    choice = input('Write action (buy, fill, take, remaining, exit):\n')
    if choice == 'buy':
        buy()
    elif choice == 'fill':
        fill()
    elif choice == 'take':
        take()
    elif choice == 'remaining':
        remaining()
    elif choice == 'exit':
        break
