#lets define our main function
def main():
    m = int(input("m:"))  #this takes the input of mass in kg
    c = int(300000000)    #this is the constant value of speed of light
    e = int(m*square(c))  #calculated Energy in joules
    print("E:", e)        #printed the value of energy

def square(c):            #here i defined a function to square the speed of light
    return c ** 2

main()
