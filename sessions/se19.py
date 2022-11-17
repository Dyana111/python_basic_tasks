'''

even=[]
for n in range(1,101):
    if(n%2==0):
        even.append(n)

print(even)
'''

'''
liEven=[]
x=0
while x<=100:
    if (x%2==0):
        liEven.append(x)
    x+=1
print(liEven)

for x in range(0,101,2):
    print (x, end=',')
'''
'''
def myeven():
    even=[]
    for n in range(1,101):
        if(n%2==0):
            even.append(n)

    return even

result=myeven()
print(result)
'''
'''
print("Prime numbers between 1 and 100 are:")
for val in range(1, 101):
  if val > 1:
    for i in range(2, val):
      if (val % i) == 0:
        break
    else:
      print(val, end=" ")
'''
'''
function [sentence]
sentence= my name is is is is mahmoud
result: my name is mahmoud

'''
s=input('please enter ur sentence:')
def noDouple(s):
   myWords=s.split(' ')
   new_words=[]
   for x in myWords:
       if x in new_words:
           continue
       else:
           new_words.append(x)
    
   print(' '.join(new_words))

noDouple(s)




























