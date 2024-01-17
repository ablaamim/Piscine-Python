import sys # import sys module to use sys.argv

def reverseSwapCase(string):                          # function to reverse and swap case
    return string.swapcase()[::-1]

#print(len(sys.argv))

if len(sys.argv) < 2:                                 # if there is no argument
    print("Usage: python exec.py <argv0> <argv1>...") # print usage
    sys.exit(0)                                       # exit the program

else:
     joined = ' '.join(sys.argv[1:])                  # join the arguments
     print(reverseSwapCase(joined))                   # print the result