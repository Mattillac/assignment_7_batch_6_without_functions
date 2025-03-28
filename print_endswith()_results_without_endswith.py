#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
def ends_with(string, suffix):
    if len(string) < len(suffix):
        return False
    return string[-len(suffix):] == suffix

text = input("Enter text: ")
text_secondary = input("Enter suffix: ")

if ends_with(text, text_secondary):
    print("True")
else:
    print("False")
#print "True" if the string ends with "World"
