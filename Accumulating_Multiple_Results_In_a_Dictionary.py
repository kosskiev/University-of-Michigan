# №1 
#Provided is a string saved to the variable name sentence. 
#Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. 
#Save this dictionary to the variable name word_counts.

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick." # some text
sentence = sentence.split() # Разделяем слова
word_counts = {} # Создаем словарь
for word in sentence:  # Перебор каждого слова в тексте
    if word not in word_counts: # Если такое слово встречается первый раз присвоить значение 0
        word_counts[word] = 0
    word_counts[word] = word_counts[word] + 1  # Прибавлять по 1 при повторении 
print(word_counts)


# №2
#Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.

stri = "what can I do"
char_d = {}
for char in stri:
    if char not in char_d:
        char_d[char] = 0
    char_d[char] = char_d[char] +1
print(char_d)
