#1:create a simple function that takes 2 numbers and print their values
def myvalues(x,y): print (x, y)

myvalues(4,6)
#2:create a simple function that takes 2 numbers and reurn their values
def myvalues2(z,t): return z,t

theNumbers= myvalues2(10,99)
print(theNumbers)
#3:In the above return function, use keyword and arguments when calling the function
def myvalues3(args=0, l=0): return args,l

theNumbers= myvalues3(10,99)
print(theNumbers)
#4:In the above return function, give x and y default values of 0 and call the
#function with no args
theNumbers= myvalues3(l=99)
print(theNumbers)
#5: Create a function that can take any number of args and print the sum of them
def mysum(args, *vartuple):
    print (args+sum(vartuple))
mysum(2,3,4,5,6,7,8,9,10)
#6:create the same sum function using the lambda & 7: call lambda on the same line
result= (lambda args, *vartuple: args+sum(vartuple))(4+sum(6,7,8,9,10,11,12,13))
print (result) #sum(vartuple) is not working here
#8:difference between local variable and global variable
'''
local variable in a function for example is only working in a function so all the
operation we make on it. it will be ineffective outside the function
but the global one : every changing whereever it is . it will be effective
'''
