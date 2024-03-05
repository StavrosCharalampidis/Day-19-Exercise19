# Function print the two args
def myFuncOne(firstArg, secondArg):
    print(f'This is the first {firstArg} ')
    print(f'And this is the {secondArg} ')
    print("End of function one \n")

# Function print like the argv 
def myFuncTwo(*args):
    script, txt = args
    print(f'The Script is {script} and you are {txt} !!!')
    print("End of function two \n")
    
    
# Some variables for myFuncOne valuse
f1 = 10
f2 = 100   

# Call the function myFuncOne  
myFuncOne(f1, f2)
myFuncOne(f1 + 30, f2 + 20)

# Some variables for myFuncTwo valuse
f1 = "ex19"
f2 = "amazing"  

# Call the function myFuncTwo
myFuncTwo(f1, f2)
myFuncTwo(f1 + ".py", f2 + " Coder")
