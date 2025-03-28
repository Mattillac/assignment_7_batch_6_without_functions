#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
def ends_with(string, suffix):
    return string[-len(suffix):] == suffix if len(string) < len(suffix) else False

text = input("Type: ")
text_secondary = input("Enter suffix: ")
#print "True" if the string ends with "World"