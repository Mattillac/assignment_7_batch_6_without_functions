#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
def ljust_string(string, character):
    if len(string) >=  character:
        return string
    return string + ' ' * ( character- len(string))

#enter "hello"
text = input("Enter text: ")    
character = int(input("Enter length: "))
#add number of spaces for ex: "9"
result = ljust_string(text, character)
print(f"Result: '{result}'")
#print "hello    "




