import math as m

def question1(text):

    #tmp is temporary data holder
    tmp = []
    #uniqueWords is to keep the words in all sentences
    uniqueWords = []
    #uniqueWordsNums is keeps how many unique keys there are in a sentence
    uniqueWordsNums = [[], [], [], []]
    #calculated idf variables is keep in "idfvalues"
    idfValues = []
    #Last calculation variables keep on tFIDValue
    tFIDFValues = [[],[],[],[]]

    for i in text:
        #split sentenceses keywords and save on tmp variable
        tmp.append(i.split())

    #tmp values save on text list
    text = tmp
    #resetting the tmp list
    tmp = []

    #We check words keeping in "uniqueWords" list,
    #if we don't keep that word in the list add to list.
    for sentence in text:
            for word in sentence:
                if not word in uniqueWords:

                    #find unique words and storage in uniqueWords list
                    uniqueWords.append(word)

    for k in range(len(text)):
            for x in  uniqueWords:

                #Scan in sentences unique keywords and how many times did contains save on numbersOfWord
                numberOfWord = text[k].count(x)
                #Find keyword index and assign to the indexOfX
                indefOfX = uniqueWords.index(x)
                #UniqueWordNums have 4 lists and we store how many unique keywords it contain
                uniqueWordsNums[k].insert(indefOfX,numberOfWord)

    #df is a variable of how many sentences have keywod
    df =0
    #w is sentence length, I use first sentence because sentences lenghts is equal for this homework
    for w in range(len(uniqueWordsNums[0])):
        #q is element of unique keyword repeat
        for q in uniqueWordsNums:

            if int(q[w]) > 0:
                df += 1

        tmp.append(df)
        df = 0

    for v in tmp:
        #We get the 3 digits of the numbers after the comma and add these values on idfValues.
        idfValues.append(float(format(idfCalculater(len(text),v), '.3f')))

    for sentence in range(int(len(uniqueWordsNums))):
        for word in range(int(len(uniqueWordsNums[sentence]))):

            tFIDFValues[sentence].append(float(idfValues[word] * uniqueWordsNums[sentence][word]))

    print(str(text).replace("],","],\n"))
    print("-"*100)
    print(uniqueWords)
    print("-" * 100)
    print(str(tFIDFValues).replace("],","],\n"))


def idfCalculater(n,df):

    #value is sentence divided by this keyword have in how much sentence.
    value = (n/df)
    print(value)
    return m.log(value,10)

if __name__ == "__main__":

    text = ["duran duran sang wild boys in 1984", "wild boys don't remain forever wild","who brought wild flowers","it was john krakauer who wrote in to the wild"]
    question1(text)