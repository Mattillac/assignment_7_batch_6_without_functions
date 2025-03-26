#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
def prefix_remover(string, prefix):
    if string.startswith(prefix):
        return string[len(prefix):]
    return string
#enter "Mr. Joestar"
text = "Mr. Joestar!"
print(prefix_remover(text, "Mr. "))
#print "Joestar"