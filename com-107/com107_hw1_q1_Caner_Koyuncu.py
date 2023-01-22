
def lowestExamGrade():
    n = int(input("How many nots will you enter? "))
    maximumGrade = int(input("Please input maximum grade note: "))
    grades = []


    for i in range(n):
        grades.append(int(input("Grade {} is: ".format(i+1))))

    print(grades)

    lowerGrade = maximumGrade
    for k in grades:
        if(k < lowerGrade):
            lowerGrade = k
            lowerGrade = k

    print(lowerGrade)
if __name__ == '__main__':
    lowestExamGrade()

