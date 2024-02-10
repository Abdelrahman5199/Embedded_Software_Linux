
#Author : Abdelrahman Kotb
# Pass by Value
def fun(x):
    x=5
    print("Inside function ",x)
    print("Inside function ",id(x))
    
x=10
print("Before function ",x)
print("Before function ",id(x))
fun(x)
print("After function ",x)
print("After function ",id(x))

#   Pass by Ref
def fun(y):
    y[0]=5
    print("Inside function ",y)
    print("Inside function ",id(y))
    
y=[10]
print("Before function ",y)
print("Before function ",id(y))
fun(y)
print("After function ",y)
print("After function ",id(y))
   