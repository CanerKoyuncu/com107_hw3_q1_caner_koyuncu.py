
def question2():

    numbers = [0]*2

    for i in range(2):

        numbers[i] = input("Please enter number {}:".format(i+1))

    isPalindromic = [False]*2

    for x in range(2):

        if len(numbers[x])==3:

            if numbers[x][0:1] == numbers[x][2:3]:
                isPalindromic[x] = True

        else:

            print("This number is not 3-digit number : {}".format(numbers[x]))

    for i in range(0, len(numbers)):

        numbers[i] = int(numbers[i])

    if(isPalindromic[0] == True and isPalindromic[1] == True):

        total = numbers[0] + numbers[1]
        print("{} + {} = {}".format(numbers[0],numbers[1],total))

    elif(isPalindromic[0] == True or isPalindromic[1] == True):

        if(isPalindromic[0] == True and isPalindromic[1] == False):

            total = numbers[0] - numbers[1]
            print("{} + {} = {}".format(numbers[0],numbers[1],total))

        else:

            total = numbers[1] - numbers[0]
            print("{} - {} = {}".format(numbers[1], numbers[0], total))

    else:

        total = numbers[0] * numbers[1]
        print("{} * {} = {}".format(numbers[0], numbers[1], total))

if __name__ == '__main__':

    question2()