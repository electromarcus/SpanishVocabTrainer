import random as rd
from deep_translator import GoogleTranslator
print("Welcome to TheVocabTrainer – – – – – – – – – –")
#language = input("Please enter the language you are learning")
def enter_words():
    file = open("spanishwords.txt", "w+")
    wordInput = ""
    print("Importance is 9 is most important, How well you know it is 9 you don't know it at all")
    while wordInput != "x":
        wordInput = input("Enter a word, its importance, and how well you know it (1-9) (x to stop): ")
        wordInput = wordInput.lower()
        if wordInput != "x":
            file.writelines(wordInput+"\n")
            print(wordInput) 

def translate_english():
    if (input("1 for Single Words, 2 for Multi-word entry")) == 1:
        words_to_translate = input("Enter the words to translate and its importance (1-9, 9 its very important): ")
        word_to_translate = words_to_translate.split()[0]
        translated = GoogleTranslator(source = 'en', target='es').translate(word_to_translate)
        with open('spanishwords.txt', 'a') as file:
            file.write(translated + " " + str(words_to_translate.split()[1]) + " 8" + '\n')
    else:
        words_to_translate = input("Enter the words to be translated: ")
        importances = input("Enter the importance of each word in order (e.g. 4 6 2 7) (1-9, 9 is most important): ")
        words_to_translate = words_to_translate.lower().split()
        words_to_translate.remove(",", ".", ":","-",'"',"'")
        with open('spanishwords.txt', 'a'):
            print("placeholder")

        

def practice_words():
    listregister = []
    with open("spanishwords.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            listregister.append(line)
            #print(line)
            #print(listregister)
        while len(listregister) > 1:
            for item in listregister:
                if len(listregister) > 1:
                    if rd.randint(1,90) > (int(item[len(item)-3])*int(item[len(item)-1])+2):
                        listregister.remove(item)

    print(listregister)
    # need to make it change over time and get user input

def analyse_paragraph():
    print("This will tell you the frequency of words in a paragraph, so enter the words and they can include punctuation and capitals.")
    paragraph = input("Enter a paragraph: ")
    paragraph = paragraph.lower()
    paragraph_edit = ""
    for letter in paragraph:
        if letter.isalpha() or (letter == " "):
            paragraph_edit += letter
    paragraph_edit = paragraph_edit.split(" ")
    print(paragraph_edit)
    paragraph_adding = []
    for word in paragraph_edit:
        found = False
        for i in range(0,len(paragraph_adding)):
            if paragraph_adding[i] == word:
                paragraph_adding[i+1] = str(int(paragraph_adding[i+1])+1)
                found = True
        if not found:
            paragraph_adding.append(word)
            paragraph_adding.append("1")
    print(paragraph_adding)
    paragraph_adding2 = []
    for iii in range(0,len(paragraph_adding)):
        if (iii % 2 == 0) or (iii == 0):
            paragraph_adding2.append(paragraph_adding[iii] + paragraph_adding[iii+1])
        print(paragraph_adding2)
    print(paragraph_adding2)
    yes = paragraph_adding2
    paragraph_adding3_temp = paragraph_adding2
    paragraph_adding3 = []
    test_case = input("Enter 1 if you want to get the top words, and 2 if you want to test yourself on the paragraph's words")


    if test_case == "1":
        commonness = (int(input("Enter the least number of times you want of a word: "))-1)
        for i in range(10,commonness-1,-1): #goes through each word and its value
            for value in paragraph_adding3_temp:
                if int(value[len(value)-1]) > i:
                    paragraph_adding3.append(value)
                    paragraph_adding3_temp.remove(value)
        print(paragraph_adding3)
        for words in paragraph_adding3:
            print("The word", words[0:(len(words)-1)], "appears", words[len(words)-1], "times")
            input("Enter what you think this word means: ")
            # Add in something to translate the word then output it

    elif test_case == "2":
        user_attempt = ""
        user_test_paragraph_register = []
        paragraph_split = paragraph.split()
        for iiii in paragraph_split:
            print(paragraph_split)
            print(iiii)
            user_test_paragraph_register.append(iiii)
            if iiii[len(iiii)-1] == ".":
                print(user_test_paragraph_register)
                user_attempt += input("Enter what you think this sentence means: " + str(" ".join(user_test_paragraph_register) + " ")) + " "
                user_test_paragraph_register = []
        print("The original paragraph was:", paragraph, "What you thought it was:", user_attempt, "What it actually is:") #translate it

print(GoogleTranslator(source='en', target='es').translate("Hello"))
print("1 - Enter New Spanish Words\n2 - Enter New English Words to be Translated\n3 - Practice the Words\n4 "
"- Enter a paragraph ")
inputChoice = input("Enter 1-4: ")
if inputChoice == "1":
    enter_words()
if inputChoice == "2":
    translate_english()
if inputChoice == "3":
    for i in range(1,20):
        practice_words()
if inputChoice == "4":
    analyse_paragraph()