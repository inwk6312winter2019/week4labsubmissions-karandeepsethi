import string
def string_things(lisofwords):
    fin= open("58782-0.txt","r")
    wordsl = open(lisofwords,"r")
    punct = string.punctuation
    histo = dict()
    counter = 0
    listofwords = []
    newlist = []
    newwords = []
    for line in fin:
        line= line.strip()
        for i in punct:
           line = line.replace(i,"")
           line= line.lower()
           line = line.split()
        	for line in fin:
            		listofwords.append(line)
    			for lists in listofwords:
       				 if lists not in histo:
            				histo[lists] = 1
        			 else:
           				histo[lists] += 1
    					for word in wordsl:
        					word = word.strip()
        					word = word.lower()
        					newwords.append(word) 
    						for key, value in histo.items():
        						if key not in newwords:
            						print(key)

a= input("Enter file name of list of words:")
string_things(a)


