def EX1_5(a):
    '''
(int)->(str)
in this function we Classifing Age by
using your age number

example:
EX1_5(0.5) ➞ Infant
'''
    if a<1 and a==1:
        return "Infant"
    elif a>1 and a<13:
        return "Child"
    elif a==13 and a>13 and a<20:
        return "teenager"
    else:
        return "adult"

