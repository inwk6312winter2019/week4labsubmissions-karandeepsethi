import string
def string_things():
    fin= open("58782-0.txt","r")
    punct = string.punctuation
    histo = dict()
    counter = 0
    listofwords = []
    for line in fin:
        line = line.strip()
        for i in punct:
           line= line.replace(i,"")
           line= line.lower()
           line= line.split()
        	for line in listofwords:
            		listofwords.append(line)
    			for lists in listofwords:
        			if lists not in histo:
           				 histo[lists] = 1
        			else:
            				histo[lists] += 1
    					for key, value in histo.items():
        					if(value == 20):
            						print(key)

string_things()


