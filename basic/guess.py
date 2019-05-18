from random import randint

while True:
    print("Guessing game You have 3 lives to guess!")
    live = 3
    com_value = randint(1, 10)
    print(str(com_value))
    lost = False
    won = False
    for i in range(3):
        userGuess = input("Guess a Number between 1 to 10 : ")
        try:
            userGuess = int(userGuess)
        except ValueError:
            print('Wrong Value!!! Insert Number')
            break
        if userGuess == com_value:
            won = True
            break
        live -= 1
        if userGuess < com_value:
            print(f'{userGuess} is lower, lives left : {live}')
        if userGuess > com_value:
            print(f'{userGuess} is higher, lives left : {live}')
        if live < 1:
            lost = True
            break

    if lost:
        inp = input("You Lost :(! << try again?(y/n)")
        if inp == 'y':
            continue
        else:
            break
    if won:
        inp = input("You Won :)! << try again?(y/n)")
        if inp == 'y':
            continue
        else:
            break