from math import fmod,sqrt

def GreatestCommonDivisor():

    if(fmod(number1, number2)==0):
        print("GDC : ", number2,"line7", sep=" ")
        
    elif(fmod(number2, number1) == 0):
        print("GDC : ", number1,"line10", sep=" ")
    
    else:
        if(number1 > number2):
            loopGDC(number1)
        elif(number2 > number1):
            loopGDC(number2)
        else:
            # if number1 and number2 is equal
            print("GDC: ", number1, " Line19")

def loopGDC(k):
    
    for i in range(k,0,-1):
        if(fmod(number1, i)==0 and fmod(number2, i)==0):
            print("GDC: ", i,"line25")
            break
         
if __name__ == '__main__':
    number1 = int(input("Please input number 1: "))
    number2 = int(input("Please input number 2: "))
    GreatestCommonDivisor()