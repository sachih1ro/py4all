# Algorithmic challenge: count of unbalanced parentheses
# Reto de Algoritmia: conteo de paréntesis desbalanceados
#
# by @sachi_h1ro (Elias Camilo Cabarcas Carreño)


#function for count uncloused parentheses "(" and ")"
def unclosedParenthesesCounter(str_parenthesis):
    countOpen = 0           #Counter for open parenthesis "(" not closed with ")"
    countUnclousable = 0    #Counter for unclouseable ")" parenthesis

    #Loop for check the string
    for par in str_parenthesis:
        
        if par == "(":
            #All "(" parentheses are openers
            countOpen += 1

        elif par == ")":
            #But all "(" parentheses are not closers
            if (countOpen > 0):
                #If we got any "(" unclosed previous, this ")" will be a closer
                countOpen -= 1
            elif (countOpen == 0):
                #But if we have a ")" with none "(" unclosed previous, we got an unclosable
                countUnclousable += 1
    
    #The unclosed are the openeds plus the unclosables
    return(countOpen + countUnclousable)


#LETS TRY!!!

str_parentesis_to_evaluate = "(()())" #str with parentheses to evaluate
numUnClosed = unclosedParenthesesCounter(str_parentesis_to_evaluate) #evaluating
print("The number of unclosed parentheses is " + str(numUnClosed)) #response
