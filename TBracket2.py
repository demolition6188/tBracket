income = 0

def percentIncome(o,i):
    return (o * 100) / i

def net(income, owe):
    return income - owe

def bracket(i, a, p):
    owe = a + i * p
    print('You owe : $'+ str(owe) + '.')
    print('You are in the : ' + str(p*100)+ '% tax bracket.')
    print('Which is ' + str(percentIncome(owe, i)) + '% of your total income.')
    print('Your net income is : $' + str(net(i, owe)) + '.')

again = True
while again:
    print('Please enter your income.')
    income = int(input())

    if income > 235350:
        bracket(income, 65814, .395)
    elif income > 208350:
        bracket(income, 56364, .35)
    elif income > 116675:
        bracket(income, 26111.25, .33)
    elif income > 76550:
        bracket(income, 14876.25, .28)
    elif income > 37950:
        bracket(income, 5226.25, .25)
    elif income > 9325:
        bracket(income, 932.5, .15)
    else:
        bracket(income, 0, .1)

    print('Would you like to estimate again? <blank for yes, anything for no>')
    again = input()
    if bool(again) == False:
        again = True
        continue
    else:
        break

