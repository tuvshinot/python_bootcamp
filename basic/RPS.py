from random import sample

options = ['rock', 'scissor', 'paper']
print("Insert (rock, scissor, paper)")
print("Insert 'done' to finish game.!")
while True:
    choice = sample(options, 1)
    choice = choice[0]
    userChoice = input("Insert RPS : ")
    if userChoice == 'rock':
        if choice == 'rock':
            print('You : ' + userChoice + '___________' + "Computer : " + choice)
            print('Tie!')
        if choice == 'paper':
            print('You : ' + userChoice + '___________' + "Computer : " + choice)
            print('You Lost!')
        if choice == 'scissor':
            print('You : ' + userChoice + '___________' + "Computer : " + choice)
            print('You Win!')
    elif userChoice == 'scissor':
        if choice == 'rock':
            print('You : ' + userChoice + '___________' + "Computer : " + choice)
            print('You Lost!')
        if choice == 'paper':
            print('You : ' + userChoice + '___________' + "Computer : " + choice)
            print('You Win!')
        if choice == 'scissor':
            print('You : ' + userChoice + '___________' + "Computer : " + choice)
            print('Tie!')
    elif userChoice == 'paper':
        if choice == 'rock':
            print('You : ' + userChoice + '___________' + "Computer : " + choice)
            print('You Win!')
        if choice == 'paper':
            print('You : ' + userChoice + '___________' + "Computer : " + choice)
            print('Tie!')
        if choice == 'scissor':
            print('You : ' + userChoice + '___________' + "Computer : " + choice)
            print('You Lost!')
    else:
        print('Finishing game!')
        break

