'''
x=1
while x<=10:
    y=1
    while y<=12:
        print (f'{x}X{y}=',x*y)
        y+=1
    x +=1

for x in [[10,20,30],[30,40,50],[60,70,80],4,5,6]:
    if type(x) != int:
        for y in x:
            print (y)
    else:
        print (x)
'''

start= int(input('please enter the start number:'))
end= int(input('please enter the end number:'))
for x in range (start, end):
    print('----------------------------------')
    for y in range (start, end):
        print(f'{x}X{y}= ', x*y)
   
