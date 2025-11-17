# Python code to illustrate 
# working of try()  
def divide(x, y): 
    try: # try block is ran to check for exceptions
        # Floor Division : Gives only Fractional 
        # Part as Answer 
        result = x // y 
    except ZeroDivisionError: # if the try block raises an error, the except block is executed
        print("Sorry ! You are dividing by zero ") 
    else: # if no exception (no erros in try block) occurs, the else block is executed
        print("Yeah ! Your answer is :", result) 
    finally:  # finally block is always executed no matter what
        # this block is always executed   
        # regardless of exception generation.  
        print('This is always executed')   

# Look at parameters and note the working of Program 
divide(3, 2) 
divide(3, 0)