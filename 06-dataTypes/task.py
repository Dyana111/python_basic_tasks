#1:what is the difference between '',"",''' '''
'''
we use all of them with the string values and the are pretty
the same, but:
we use '' if we have a normal str
we use "" if we need to use in the str '
for example: s="it's beautiful"
we use '' ' if we have a text (more than one line)
'''
#2:Create a string with the name 'mystro'
name='mystro'
#3:Make the string latter Capital:
s1=name.upper()
print(s1)
#4:create a list of values from 10 to 20
numbers=[x for x in range(10,21)]
print (numbers)
#5: add 30 to the end of the list:
numbers.append(30)
print (numbers)
#6:add 40 as the second element of the list:
numbers.insert(1,40)
print(numbers)
#7:print how many elements in the list:
print(len(numbers))
#8:replace  the second element in the list with 100:
numbers[1]=100
print(numbers)
#9:Create a tuple with values from 1 to 5:
numbers2=(1,2,3,4,5)
#10: can we add 10 to the end of the tuple:
'''no'''
#11:create a dict of value Mahmoud:28, ahmed:30
dic={'Mahmoud':28, 'ahmed':30}
#12:print Mahmouds age from the dict:
print(dic['Mahmoud'])
