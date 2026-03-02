with open("task1.txt", "r") as f:
    text = f.read()

symbol = ['@', '#', '$', '%', '&', '*', '(',  '-', '_', '=',')', '+']
penctuation = ['.', ',', '!', ';', '?', ':', '"', '/',"'",  '\\']

nouveaux_text  = ""

for charactere in text:
    if charactere.isdigit():
        continue
    if charactere in symbol :
        nouveaux_text += " "
    if charactere in penctuation:
        nouveaux_text += " "
    else:
        nouveaux_text  += charactere.lower()

nouveaux_text  = nouveaux_text .split()
nouveaux_text  = " ".join(nouveaux_text )
print(nouveaux_text )


import re
phrase = "\nHe scored 88% and %% won the 1%st and 2nd game\n"
phrase = re.sub(r'(?<!\d)%+','',phrase)
phrase = re.sub(r'(\d)%([a-zA-Z]+)',r'\1\2',phrase)
print(phrase)


nembres = {'0':'zero','1':'one','2':'two','3':'three','4':'four',
           '5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

texte = "\nWow!! This cow ran fast & ate 3 apples."

new = ""
for ch in texte:
    if ch.isdigit():
        new += " " + nembres[ch] + " "
    elif ch.isalpha() :
        new += ch.lower()
    elif ch == " ":
        new += ch.lower()

new=new .split()
new=" ".join(new )
print(new+"\n")


texte = "\nI'm sure the cow will stop the ducks from fighting soon!!."
texte = texte.replace("I'm", "I am")
new = ""
for ch in texte:
    if ch.isalpha() :
        new += ch.lower()
    elif ch == " ":
        new += ch.lower()

new=new .split()
new=" ".join(new )
print(new)

with open("task2.txt", "r") as f:
    text = f.read()
text = text.replace("I'm", "I am")

new = ""
for char in text:
    if char.isdigit():
        continue
    if char.isalpha() or char == " ":
        new += char.lower()

new = " ".join(new.split())
print(new)



def normaliser(texte):
    nembres = {'0':'zero','1':'one','2':'two','3':'three','4':'four',
           '5':'five','6':'six','7':'seven','8':'eight','9':'nine'}


    new = ""
    for ch in texte:
        if ch.isdigit():
            new += " " + nembres[ch] + " "
        elif ch.isalpha() :
            new += ch.lower()
        elif ch == " ":
            new += ch.lower()

    new=new .split()
    new=" ".join(new )
    return new


D1 = "Today she cooked 4 bourak. Later, she added two chamiyya and 1 pizza."
D2 = "Five pizza were ready, but 3 bourak burned!"
D3 = "We only had 8 chamiyya, no pizza, and one tea."
D4 = "Is 6 too much? I ate nine bourak lol."

test= [D1, D2, D3, D4]
i=1
for  char in test:
    i=i+1
    print(f"D{i}:", normaliser(char))





#line 10
# use string.punctuation bcz it saves you from typing all those marks
    
# line 13
# instead of separate if statements for symbols and punctuation, use one elif
# or just check if the char is in both lists at once
    
# line 30
# using regex re.sub is good, but make sure you understand the lookbehind (?<!\d)
# it's a bit advanced if you haven't studied it yet
    
# line 47
# building strings with += inside a loop is discouraged bcz strings are immutable
# use a list and then .join() for better performance
    
# line 56
# manually replacing "I'm" only works for one case
# use a dictionary for contractions if you want to handle "don't", "can't", etc

#It feels like you wrote the simple parts and asked an AI to do the rest
#No need for AI when the task is this brain-dead simple. Try to actually code next time 
