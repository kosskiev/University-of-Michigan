words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []

for i in range(len(words)):
    if words[i][-1:] == 'e':
        words[i] += "d"
        past_tense.append(words[i])
    else:
        words[i] += "ed"
        past_tense.append(words[i])
print(past_tense)

