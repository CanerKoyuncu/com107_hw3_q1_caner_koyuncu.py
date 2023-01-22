
def question1(sentence):

    if type(sentence) == str :
        #If parameter is a string.

        print("Sentence: " + sentence)
        sentence = sentence.split(" ")

        for i in range(len(sentence),0,-1):
            print(str(sentence[i-1][::-1]))

    else:
        #if parameter is a not string.
        print("Please enter a string value!!!")


if __name__ == "__main__":

    question1("I want to fix my car")