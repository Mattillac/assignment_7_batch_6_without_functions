#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
def ljust_string(string, length):
    if len(string) >= length:
        return string
    return string + ' ' * (length - len(string))

#enter "hello"
#add number of spaces for ex: "9"
#print "hello    "




