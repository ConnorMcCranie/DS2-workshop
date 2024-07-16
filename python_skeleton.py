# Here's my imports
import numpy as np

#################################

# Here are my functions

def func_1():
    # does something 
    return 0

def func_2():
    # does something else
    return 1

# etc.


###################################

# Here's the deifnition for my main function

def main():
    # does something using the functions above
    if func_2() >= func_1():
        print('This program is working!')
        return np.pi
    else:
        return np.pi-10**-10



###################################

if __name__ == "__main__":
    main()