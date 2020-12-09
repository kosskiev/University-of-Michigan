#The string module provides sequences of various types of Python characters. It has an attribute called digits that produces the string ‘0123456789’. 
#Import the module and assign this string to the variable nums. Below, we have provided a list of characters called chars. 
#Using nums and chars, produce a list called is_num that consists of tuples. 
#The first element of each tuple should be the character from chars, and the second element should be a Boolean that reflects whether or not it is a Python digit.

#I do not use -  num = string.digits
import string 
chars = ['h', '1', 'C', 'i', '9', 'True', '3.1', '8', 'F', '4', 'j'] #some text
num = string.digits

is_num = ()
spisok1 = []
for i in range(len(chars)):
    spisok = ()
    if chars[i].isdigit():
        spisok += (chars[i], True)
        spisok1.append(spisok)
    else:
        spisok += (chars[i], False)
        spisok1.append(spisok)
is_num = spisok1
print(is_num)
