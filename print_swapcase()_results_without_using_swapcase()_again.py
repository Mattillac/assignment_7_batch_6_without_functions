#Prog09. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
def bootleg_swapcase(string):
    case_changer = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return string.translate(case_changer)
#enter "wAIT aNd bLEED"
text = input("Enter text: ")
print(bootleg_swapcase(text))
#print "Wait And Bleed"