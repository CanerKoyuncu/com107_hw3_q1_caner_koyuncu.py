# Code snippet to reverse the entire sentence
# The final state of the sentence as a string needs to be returned
def fn1(sentence):
    reversedSentence = sentence[::-1]
    return reversedSentence

# Code snippet to reverse the entire sentence
# If the sentence is reversed, lowercase letters will change to uppercase and uppercase letters to lowercase.
# The final state of the sentence as a string needs to be returned
def fn2(sentence):
    sentence = fn1(sentence)

    return sentence.swapcase()

# Code that reverses every word in the sentence within itself
# The final state of the sentence as a string" needs to be returned
def fn3(sentence):
    tmp1 = fn1(sentence).split(" ")[::-1]
    sentence = ' '.join(map(str,tmp1))

    return sentence

# Code that prints lowercase and uppercase letters in a sentence in 2 groups with spaces in between
# Lowercase and uppercase letters must be printed sequentially.
# Result needs to be returned as String
def fn4(sentence):

    tmp1 = sentence.replace(" ", "")

    uppercases = []

    for letter in sentence:
        if letter.isupper():
            tmp1 = tmp1.replace(letter, "")
            uppercases.append(letter)

    return (tmp1 + " " + "".join(uppercases))

# Code to sort each word in the sentence alphabetically
# The final state of the sentence as a string needs to be returned
def fn5(sentence):
    tmp1 = " "
    tmp2 = []
    sentence = sentence.split(" ")
    for word in sentence:
        tmp2.append("" + "".join(sorted(word)))
    result = tmp1.join(tmp2)
    return result


hw_grade = 0

fn1TestGirdi=['Okula geldim', 'Akşam eve gideceğim']
fn1TestCikti=['midleg alukO', 'miğecedig eve maşkA']

hw_grade = hw_grade + 20
for i in range(len(fn1TestGirdi)):
    sonuc = fn1(fn1TestGirdi[i])
    if (sonuc!=fn1TestCikti[i]):
        hw_grade = hw_grade - 10

print("After 1. question:", hw_grade)

fn2TestGirdi=['Okula Geldim', 'AkşaM Eve GiDeceğim']
fn2TestCikti=['MIDLEg ALUKo', 'MIĞECEdIg EVe mAŞKa']

hw_grade = hw_grade + 20
for i in range(len(fn2TestGirdi)):
    sonuc = fn2(fn2TestGirdi[i])
    if (sonuc!=fn2TestCikti[i]):
        hw_grade = hw_grade - 10

print("After 2. question:", hw_grade)

fn3TestGirdi=['The train was late', 'Joe waited for the train']
fn3TestCikti=['ehT niart saw etal', 'eoJ detiaw rof eht niart']

hw_grade = hw_grade + 20
for i in range(len(fn3TestGirdi)):
    sonuc = fn3(fn3TestGirdi[i])
    if (sonuc!=fn3TestCikti[i]):
        hw_grade = hw_grade - 10

print("After 3. question:", hw_grade)

fn4TestGirdi=['The TraiN waS late', 'Joe waited for the train']
fn4TestCikti=['heraiwalate TTNS', 'oewaitedforthetrain J']

hw_grade = hw_grade + 20
for i in range(len(fn4TestGirdi)):
    sonuc = fn4(fn4TestGirdi[i])
    if (sonuc!=fn4TestCikti[i]):
        hw_grade = hw_grade - 10

print("After 4. question:", hw_grade)

fn5TestGirdi=['you can go faster than 150', 'dikkatli yolculuk']
fn5TestCikti=['ouy acn go aefrst ahnt 015', 'adiikklt ckllouuy']

hw_grade = hw_grade + 20
for i in range(len(fn5TestGirdi)):
    sonuc=fn5(fn5TestGirdi[i])
    if (sonuc!=fn5TestCikti[i]):
        hw_grade = hw_grade - 10

print("After 5. question:", hw_grade)
