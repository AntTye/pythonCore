# For all possible uses of python variables.

#unbinded variable
#causes NameError because x is not defined.
x

#This is a basic assignment where x is on stack "points to" 10 is on heap
# 10 is immutable but x is allowing x + 5
x = 10

#a references the same memory location as x.
# a -> x -> heap 10
a = x

#rebinds a variable with a new object at a new location
#a still points to the original memory location of the original object
x = 1


#Both ls1 and ls2 point to same location in memory resulting in modification of both variables. the List [1,2,3] is located on the heap, pointed to by ls1 and ls2.
ls1 = [1,2,3]
ls2 = ls1
ls1.append(4)

### Understand the scope of these variables

#more within the functions.py but variables are capible to be function parameters
#we define a function with def _( ) :
#all variables are only within the functions local namespace scope.
#any rebinds does not affect original variable
#dud function because it simply has no substance
def foo ( variable1 ) :
    variable1 = 100

x = 200


x = 10

# recieves x = 10, rebinds at local to make x = 99 but the global x is still 10
def fee(x):
    x = 99  # Rebinding local x only no interaction with x = 10.



foo(x)    #nothing because we do not assign outside of function, no return or print
print (x) #still points to memory location of x when it points to 100

#We can delete the reference if needed to make varaible undefined
x = 5
del x

#Global varaibles are outside the scope of the local function. 
#To alter global variables within local functions we use the Global tag to the varaible to lift it into the global state.
index = 0

def increment():
    global index
    index += 1

#Nonlocal variables are within the scope of the local function, lifted from within to a higher priority. Think of it as a sink hole with steps into the middle of the hole, where the flat ground level before any steps is the global, each step into the center of the hole in is seen as its local scope.
#In this case there is the the flat ground, and 2 steps inside. Step 2 will not interact with Step 1 unles we lift it above, step out. In global we can directly jump out to the flat ground level:
x = 0

def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
    inner()
    print(x)  # 2
