
#function for count uncloused parentheses "(" and ")"
def unclosedParenthesesCounter(str_parenthesis):
    countOpen = 0           #Counter for open parenthesis "(" not closed with ")"
    countUnclousable = 0    #Counter for unclouseable ")" parenthesis

    #Loop for check the string
    for par in str_parenthesis:
        #All "(" parentheses are openers
        if par == "(":
            countOpen += 1

        elif par == ")":
            #But all "(" parentheses are not closers
            if (countOpen > 0):
                #If we got any "(" unclosed previous, this ")" will be a closer
                countOpen -= 1
            elif (countOpen == 0):  # reemplazable por else
                countUnclousable += 1

    return(countOpen + countUnclousable)


#LETS TRY!!!

str_parentesis_to_evaluate = "(()())" #str with parentheses to evaluate
numUnClosed = unclosedParenthesesCounter(str_parentesis_to_evaluate) #evaluating, dah
print("The number of unclosed parentheses is " + str(numUnClosed)) #response