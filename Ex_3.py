def EX1_3(a,b):
'''
(int,int)->(int)
in this function we are calculating Maximum
Edge of a Triangle

example:
EX1_3(8, 10) ➞ 17

'''
  if type(side1) == int and type(side2) == int:
       if a>0 and b>0:
        answer=a+b-1
        return answer
       else:
         answer="Such triangle dose not exist!"
         return answer
  else:
         answer="Such triangle dose not exist!"
         return answer
