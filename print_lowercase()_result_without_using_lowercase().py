#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
def lower_caser(text):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    translated_text = str.maketrans(uppercase, lowercase)
    return text.translate(translated_text)

#enter "ACCESS DENIED"
#print "access denied" without using lower() function