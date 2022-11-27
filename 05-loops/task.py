
#1: Print numbers from 0 to 10 using while:
x=0
while x<=10:
    print (x)
    x+=1
#2:print numbers from 0 to 10 using for:
for x in range(11):
    print(x)
#3: stop the loop if the number=5:
for x in range(11):
    print(x )
    if x==5:
        break
#4:skip the 5 iteration from print:
for x in range(11):
    if x==5:
        continue
    print (x)
#5:print multiplication table from 1 to 5
for x in range(1,6):
    for y in range(1,11):
        print(f"{x}X{y}= {x*y}")
#6:How to get numbers from 10 to 20 using range:
for x in range(10,21):
    print (x)
#7:How to get numbers from 10 to 100 with 3 at each step using range:
for x in range (10,101,3):
    print (x)
    
#8:Get a list of even numbers from 1 tp 100 using for:

def even():
    ev=[]
    for x in range (1,101):
        if x%2==0:
            ev.append(x)
        else:
            continue
    return(ev)

evenNumberCheck=even()
print(evenNumberCheck)

#9: get a list of even numbers from 1 to 100 using while:

def evenCheck():
    evenNum=[]
    x=1
    while x<=100:
        if x%2!=0:
            continue
        else:
            evenNum.append(x)
        x+=1
    print(evenNum)


evenCheck()

#10: git a list of even numbers from 1 to 100 using range:
evenCheck=[]
for x in range(0,101,2):
    evenCheck.append(x)
print (evenCheck)
