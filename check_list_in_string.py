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
