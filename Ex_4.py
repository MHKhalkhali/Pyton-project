def EX1_4(a):
    '''
    (int)->(str)
    in this function we calculate the day of the week with day number
    example:
    EX1_4(2) ➞ Tuesday
    '''
    if a==1:
        return "Monday"
    elif a==2:
        return "Tuesday"
    elif a==3:
        return "Wednesday"
    elif a==4:
        return "Thursday"
    elif a==5:
        return "Friday"
    elif a==6:
        return "Saturday"
    elif a==7:
        return "Sunday"
    else:
        return"your number can between 1 to 7 !"
