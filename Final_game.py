def JPgame():
    print('Hello we are going to play a game.\n'
          'In this game I will attempt to guess your number between 1 and 1000000.\n'
          'Please enter a number after the first propmt,\n'
          'after the I make the first guess please respond with\n'
          'a H if your number is higher and L if you number\n'
          'number is lower or a C if i guessed correctly.')

    Low= 1
    High= 1000000
    countGuess= 0
    countGame= 1

    input('Please enter a number: ')

    while True:

        guess= (Low + High) // 2

        correctGuess = input('%s: ' % guess)

        if correctGuess == 'C':
                print('This is you number')
                countGuess += 1
                countGame +=1
                print('It took %s to guess you number ' % countGuess)
                print('I averaged', countGuess/countGame, 'guesses per', countGame, 'game(s)')
                continueGame= input('Play again (y/n): ')
                if continueGame == 'y':
                    JPgame()
                else:
                    print('Thanks for playing my game')
                break
        elif Low == High:
            print('No more possible answers')
            break
        elif correctGuess == 'L':
            High= guess - 1
            countGuess += 1
        elif correctGuess == 'H':
                Low= guess + 1
                countGuess += 1
        else:
                input('Does not compute... Try Again')
                
