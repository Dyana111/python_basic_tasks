'''
name= 'diana'
age=30
print(f'my name is {name} and i am {age} years old')


words=input('enter ur sentence:')
def no_dupl(sentence):
    
    li=sentence.split(' ')
    newWords=[]
    for x in li:
        if x in newWords:
            continue
        newWords.append(x)
        
    return newWords

print(' '.join(no_dupl(words)))



def no_dupl_count(sentence):
    
    li=sentence.split(' ')
    newWords=[]
    for x in li:
        if x in newWords:
            continue
        newWords.append(x)
        
    return newWords

print(len(no_dupl_count(words)))
'''
'''
a= int(input('please enter ur Number1:'))
b= int(input('please enter ur Number2:'))

def div(x,y):
    numbers=[]
    for n in range(1,101):
        if all([n%x==0,n%y==0]):
            numbers.append(n)
    return numbers

#print(div(a,b))







def div2(x,y):
    numbers=[]
    for n in range(x+1):
        if n%y==0:
            numbers.append(n)
    return numbers

#print(div2(a,b))

def sorti():
    number= input('enter Numbers:')
    newNumbers=number.split(',')
    intNumbers=[]
    for n in newNumbers:
        intNumbers.append(int(n))
    print(intNumbers)
    even=[]
    odd=[]
    for x in intNumbers:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)

    print(even, odd)
    
sorti()

'''

even=[x for x in range(1, 101) if x%2==0]



names=['ahmed', 'ali', 'adam', 'raed']

a=[x.upper() for x in names]


cn=[len(x) for x in names]

numbers=(range(1,101))
result=[True if x%2==0 else False for x in numbers]

print(result)










































































