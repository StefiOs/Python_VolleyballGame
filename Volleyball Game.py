print('This program will track the scroes in a volleyball game.')
match1team1 = eval(input('Enter the score that team 1 got on match 1? '))
match1team2 = eval(input('Enter the score that team 2 got on match 1? '))
match2team1 = eval(input('Enter the score that team 1 got on match 2? '))
match2team2 = eval(input('Enter the score that team 2 got on match 2? '))
match3team1 = eval(input('Enter the score that team 1 got on match 3? '))
match3team2 = eval(input('Enter the score that team 2 got on match 3? '))
match4team1 = eval(input('Enter the score that team 1 got on match 4? '))
match4team2 = eval(input('Enter the score that team 2 got on match 4? '))
match5team1 = eval(input('Enter the score that team 1 got on match 5? '))
match5team2 = eval(input('Enter the score that team 2 got on match 5? '))

def winner():
    if match1team1 > match1team2:
        return ('Team 1')
    else:
        return ('Team 2')

def winner2():
    if match2team1 > match2team2:
        return ('Team 1')
    else:
        return ('Team 2')

def winner3():
    if match3team1 > match3team2:
        return ('Team 1')
    else:
        return ('Team 2')

def winner4():
    if match4team1 > match4team2:
        return ('Team 1')
    else:
        return ('Team 2')

def winner5():
    if match5team1 > match5team2:
        return ('Team 1')
    else:
        return ('Team 2')
        
print("{0:>18} {1:>18} {2:>18}".format('Team 1', 'Team 2', 'Winner'))
print("{0} {1:^12} {2:^25} {3:^13}".format('Match 1', match1team1, match1team2, winner()))
print("{0} {1:^12} {2:^25} {3:^13}".format('Match 2', match2team1, match2team2, winner2()))
print("{0} {1:^12} {2:^25} {3:^13}".format('Match 3', match3team1, match3team2, winner3()))
print("{0} {1:^12} {2:^25} {3:^13}".format('Match 4', match4team1, match4team2, winner4()))
print("{0} {1:^12} {2:^25} {3:^13}".format('Match 5', match5team1, match5team2, winner5()))

if (match1team1+match2team1+match3team1+match4team1+match5team1) > (match1team2+match2team2+match3team2+match4team2+match5team2):
    print ('Winner is Team 1.')
else:
    print ('Winner is Team 2.')
