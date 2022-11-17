#1:check if 10 is bigger than 15 or not
x=10
if(x> 15):
    print('it is bigger')

else:
    print("no it's not")
#2:if 10 is not bigger than 15 print x is smaller than 15
x=11
if(x> 15):
    print('it is bigger')

else:
    print(" x is smaller than 15")
#3: in which cases we will use all
    '''
we use all when we have more than one condition and all of
them have to be true in the same time
'''
#4: what is the difference between all, and
    '''
we write if all([ cond1, cond2, cond3])
and we write if (cond1 and cond2 and cond3)
but in the meaning.. i cannot see any difference
'''
#5:what is the difference between any, or
    '''
we write if any([ cond1, cond2, cond3])
and we write if (cond1 or cond2 or cond3)
but in the meaning.. i cannot see any difference
'''
#6: if we need all the conditons to be true we will use...
   ''' 
all , and
'''
#7:what is the difference between if, elif
   '''
we can only use one if but elif could be repeated more than one time
'''
#8:difference between elif, else
  ''' 
after the elif we have to put a condition but not after the else
'''
#9:more than one elif?
  '''
yes
'''
#10:more than one else?
  '''
nope
'''
#11:write a simple ternary operator(if and else in one line)
z=input('true or false?')
print('i did it') if z=='true' else print('wrong')
#12: in elif, python will check all the conditions no matter what
'''
all the conditions after elif and between the () in case the if condition didnot
matche
'''
#13: in elif we use else for ..?
'''
to give a default option in case no condition matches, else condition will
executed
'''
#14: if we have the list [2,4,6,8,10]
    #1. check if 4 in the list or not
li=[2,4,6,8,10]
print('4 is in the list') if (4 in li) else print('4 is not in the list')
    #2. is 4 and 6 in the list or not
print('4 and 6 is in the list') if all([4 in li, 6 in li]) else print('4 and 6 is not in the list')
    #3. is 3 or 6 in the list
print('3 or 6 is in the list') if any([3 in li, 6 in li]) else print('3 or 6 is not in the list')
    #4. is 2, 4, and 5 in the list
print('2, 5 and 6 is in the list') if all([2 in li, 5 in li, 6 in li]) else print('at least one of 2,5,6 is not in the list')
