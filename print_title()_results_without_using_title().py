#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
import string
#enter "yOguRt yUM"
text = input("Enter text: ")
#print "Yogurt Yum"
print (string.capwords(text))