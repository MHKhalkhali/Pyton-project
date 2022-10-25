def EX1_6(a):
    '''
(int)->(int)
in this function we transfer english numbers between 1 to 10
to  Roman Numerals

example:
EX1_5(1) ➞ I
EX1_5(10) ➞ Error
'''
    if a==1:
        return "I"
    elif a==2:
        return "II"
    elif a==3:
        return "III"
    elif a==4:
        return "IV"
    elif a==5:
        return "V"
    elif a==6:
        return "VI"
    elif a==7:
        return "VII"
    elif a==8:
        return "VIII"
    elif a==9:
        return "IX"
    elif a==10:
        return "X"
    else:
        return "You should enter a number between 1 to 10 !"
