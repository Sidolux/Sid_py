from random import randint, seed

seed()  # seed random generator
number = randint(1, 100)  # generate number 1-100
# initiate vars
usr_guess = None
guess_count = 1
diff_old = 0
print(number) # for debug only
print('-'*95)
print('Myślę o liczbie 1-100. Spróbuj ją odgadnąć.')
print('Powiem Ci "Ciepło" jeżeli za pierwszym razem będziesz bliżej niż 10 od liczby, o której myślę.')
print('Dodatkowo przy każdej próbie powiem Ci, czy jesteś bliżej czy dalej niż poprzednio.')
print('Aby zakończyć grę napisz quit')
print('Zaczynajmy')
print('-'*95)
# Main game loop
while not usr_guess == number:  # play until player guesses the number
    usr_input = input('Podaj liczbę całkowitą 1-100: ')
    try:
        usr_guess = int(usr_input)  # get player input
    except:
        if str(usr_input).lower() == 'quit':
            break
        print('To nie jest liczba całkowita')  # check if player input is number
        continue
    if usr_guess == number:
        print(f'Gratuluję, zgadłeś w {guess_count} próbach!!!')  # Show congratulations with guesses count
        break
    if usr_guess < 1 or usr_guess > 100:  # check if player input is in range (1-100)
        print('Podałeś liczbę spoza zakresu')
        continue
    diff_current = abs(usr_guess - number)  # calculate difference between player input and generated number
    if guess_count == 1:  # on first try give hint WARM if guess is within 10, COLD if further than 10
        if diff_current <= 10:
            print('Ciepło')
        else:
            print('Zimno')
    else:
        if diff_current < diff_old:  # on all subsequent tries give WARMER/COLDER hint
            print('Cieplej')
        elif diff_current > diff_old:
            print('Zimniej')
        else:
            print('Jesteś tak samo blisko')
    diff_old = diff_current  # store old difference
    guess_count += 1  # increment guess count
print('-'*41+' KONIEC GRY  '+'-'*41)
