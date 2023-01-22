
def question2():

    numbers = [0]*2

    for i in range(2):

        numbers[i] = input("Please enter number {}:".format(i+1))

    isPalindromic = [False]*2

    for x in range(2):

        if numbers[x][0:1] == numbers[x][2:3]:
            isPalindromic[x] = True

    for i in range(0, len(numbers)):

        numbers[i] = int(numbers[i])

    if(isPalindromic[0] and isPalindromic[1]):

        total = numbers[0] + numbers[1]
        print("{} + {} = {}".format(numbers[0],numbers[1],total))

    elif(isPalindromic[0] or isPalindromic[1] ):

        if(isPalindromic[0] and not isPalindromic[1]):

            total = numbers[0] - numbers[1]
            print("{} - {} = {}".format(numbers[0],numbers[1],total))

        else:

            total = numbers[1] - numbers[0]
            print("{} - {} = {}".format(numbers[1], numbers[0], total))

    else:

        total = numbers[0] * numbers[1]
        print("{} * {} = {}".format(numbers[0], numbers[1], total))

if __name__ == '__main__':
    
    question2()