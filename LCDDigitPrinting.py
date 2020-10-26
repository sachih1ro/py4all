# Algorithmic challenge: LCD digit printing
# Reto de Algoritmia: impresión de dígitos tipo LCD
#
# by @sachi_h1ro (Elias Camilo Cabarcas Carreño)


# Bases for digit printing
#                           0                1                2                3                4
numBaseUp =         [[" ", "-", " "], [" ", " ", " "], [" ", "-", " "], [" ", "-", " "], [" ", " ", " "]]
numBaseIntUp =      [["|", " ", "|"], [" ", " ", "|"], [" ", " ", "|"], [" ", " ", "|"], ["|", " ", "|"]]
numBaseMid =        [[" ", " ", " "], [" ", " ", " "], [" ", "-", " "], [" ", "-", " "], [" ", "-", " "]]
numBaseIntDown =    [["|", " ", "|"], [" ", " ", "|"], ["|", " ", " "], [" ", " ", "|"], [" ", " ", "|"]]
numBaseDown =       [[" ", "-", " "], [" ", " ", " "], [" ", "-", " "], [" ", "-", " "], [" ", " ", " "]]

#                           5                6                7                8                9
numBaseUp +=        [[" ", "-", " "], [" ", "-", " "], [" ", "-", " "], [" ", "-", " "], [" ", "-", " "]]
numBaseIntUp +=     [["|", " ", " "], ["|", " ", " "], [" ", " ", "|"], ["|", " ", "|"], ["|", " ", "|"]]
numBaseMid +=       [[" ", "-", " "], [" ", "-", " "], [" ", " ", " "], [" ", "-", " "], [" ", "-", " "]]
numBaseIntDown +=   [[" ", " ", "|"], ["|", " ", "|"], [" ", " ", "|"], ["|", " ", "|"], [" ", " ", "|"]]
numBaseDown +=      [[" ", "-", " "], [" ", "-", " "], [" ", " ", " "], [" ", "-", " "], [" ", "-", " "]]


# Function for generate each digit in value (without vertical repetition)
def generateDigit(size, number, isFirst):
    # Left part
    if isFirst:
        textUp = numBaseUp[number][0]
        textIntUp = numBaseIntUp[number][0]
        textMid = numBaseMid[number][0]
        textIntDown = numBaseIntDown[number][0]
        textDown = numBaseDown[number][0]
    else:
        textUp = " " + numBaseUp[number][0]
        textIntUp = " " + numBaseIntUp[number][0]
        textMid = " " + numBaseMid[number][0]
        textIntDown = " " + numBaseIntDown[number][0]
        textDown = " " + numBaseDown[number][0]

    # Center part
    for i in range(size):
        textUp += numBaseUp[number][1]
        textIntUp += numBaseIntUp[number][1]
        textMid += numBaseMid[number][1]
        textIntDown += numBaseIntDown[number][1]
        textDown += numBaseDown[number][1]

    # Right part
    textUp += numBaseUp[number][2]
    textIntUp += numBaseIntUp[number][2]
    textMid += numBaseMid[number][2]
    textIntDown += numBaseIntDown[number][2]
    textDown += numBaseDown[number][2]

    # Return
    return textUp, textIntUp, textMid, textIntDown, textDown


# Function for generate the text (all digits) using LCD digits
def generateText(size, value):

    valueStr = str(value)
    digitList = list(valueStr)

    # Final text init
    text0 = ""
    text1 = ""
    text2 = ""
    text3 = ""
    text4 = ""
    countFirst = 0

    # Generating all digits (without vertical repetition)
    for digit in digitList:
        text = generateDigit(size, int(digit), countFirst == 0)
        text0 += text[0]
        text1 += text[1]
        text2 += text[2]
        text3 += text[3]
        text4 += text[4]
        countFirst += 1

    # Adding vertical repetition
    baseText1 = text1
    baseText3 = text3
    for i in range(size - 1):
        text1 += "\n" + baseText1
        text3 += "\n" + baseText3

    # Final print
    print(text0)
    print(text1)
    print(text2)
    print(text3)
    print(text4)


# Main function
def executeLCDDigitConverter():
    while True:
        entrada = input("Enter an entry: ")
        size = int(entrada.split(",")[0])
        value = int(entrada.split(",")[1])
        if (size > 0):
            generateText(size, value)
        elif ((size == 0) and (value == 0)): # "0,0" for finish the app
            print("Execution finished, goodbye.")
            break
        else:
            print("Enter valid values (with the structure: size, number) ")
            print("size and number are integers.")
            print("size must be greater than 0.")


# Execution
executeLCDDigitConverter()
