#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels.
#For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun" #Some text
vowels = ['a','e','i','o','u'] #vowels
s = ' '.join(s) 
s = s.split()
num_vowels = 0
for i in range(len(s)):
    for u in range(len(vowels)):
        if vowels[u] in s[i]:
            num_vowels += 1
print(num_vowels)

