# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def reverse(bracket):
    if(bracket == "(" or bracket == ")"):
        return ")" if bracket == "(" else "("
    elif(bracket == "{" or bracket == "}"):
        return "}" if bracket == "{" else "{"
    else:
        return "]" if bracket == "[" else "["
        
def Balanced(input):
    stack = []
    stack.append(input[0])
    for i in range(1, len(input)):
        if(len(stack) > 0):
            print(stack, "----", input[i], reverse(input[i]))
            print("Length Stack: ", len(stack), ", Reverse input[i] == stack[-1]: ", reverse(input[i]) == stack[-1] )
        if(len(stack)>0 and reverse(input[i]) == stack[-1]):
            print("here")
            stack.pop()
        else:
            stack.append(input[i])
        print(stack, "\n")
    return stack
    
print("Balanced" if len(Balanced("(()()(()"))<1 else "Unbalanced")