import string
def string_things():
    fin = open("words.txt")
    punc = string.punctuation
    for line in fin:
        line = line.strip()
        line = line.replace(" ","")
        for i in punc:
           line= line.replace(line,"")
        line= line.lower()
        return(line)

print(string_things())
