#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
text = input("Enter text: ")
#example "MIDDLE"
middle_maker = int(input("Enter length: "))
centered_text = f"{text:^{middle_maker}}"
#PRINT "   MIDDLE   "
print(centered_text)


