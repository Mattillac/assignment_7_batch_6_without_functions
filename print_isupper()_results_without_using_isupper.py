#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
def cap_checker(string):
    for char_check in string:
        if char_check.islower():
            return False
    return True
#enter "STATIKK SHIV"
text = input("Enter text: ")
print("Result:", cap_checker(text))
#PRINT TRUE
