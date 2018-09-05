from random import randint, seed

seed()  # seed random generator
number = randint(1, 100)  # generate number 1-100
# initiate vars
guess = None
guess_count = 1
diff_old = 0
print(number)
# Main game loop
while not guess == number:  # play until player guesses the number
    try:
        guess = int(input('Podaj liczbę 1-100: '))  # get player input
    except:
        print('To nie jest liczba')  # check if player input is number
        continue
    if guess == number:
        break
    if guess < 1 or guess > 100:  # check if player input is in range (1-100)
        print('Podałeś liczbę spoza zakresu')
        continue
    diff_current = abs(guess - number)  # calculate difference between player input and generated number
    if guess_count == 1:  # on first try give hint WARM if guess is within 10, COLD if further than 10
        if diff_current <= 10:
            print('Ciepło')
        elif diff_current > 10:
            print('Zimno')
    else:
        if diff_current < diff_old:  # on all subsequent tries give WARMER/COLDER hint
            print('Cieplej')
        elif diff_current > diff_old:
            print('Zimniej')
    diff_old = diff_current  # store old difference
    guess_count += 1  # increment guess count
print(f'Gratuluję, zgadłeś w {guess_count} próbach!!!')  # Show congratulations with guesses count
