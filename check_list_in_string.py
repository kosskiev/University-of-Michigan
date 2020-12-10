#Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. 
#Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. 
#Words that should not be included in the acronym are stored in the list stopwords. 
#For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"] #some list
org = "The organization for health, safety, and education"  #some text
org = org.split() #split text 
arco1 = []
for i in range(len(org)): 
    num = 0
    for n in range(len(stopwords)):
        if stopwords[n] != org[i]:
            num +=1
            if num == len(stopwords):
                arco1.append(org[i][0])
            else:
                continue
        else:
            continue
acro = ''.join(arco1).upper()    
        
print(acro)
