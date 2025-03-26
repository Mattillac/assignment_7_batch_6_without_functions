#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
def remove_space(string):
    counter = 0
    while counter < len(string) and string[counter] == ' ':
        counter += 1
    return string[counter:]
#enter "  hello world"
result = input("Enter name: ")
print ("Result:", remove_space(result))
#print "hello world" without using lstrip() function