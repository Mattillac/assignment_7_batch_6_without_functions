#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
def ends_with(string, suffix):
    if len(string) < len(suffix):
        return False
    return string[-len(suffix):] == suffix
#enter "Hello World"
#print "True" if the string ends with "World"