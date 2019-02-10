import string
def remove_pattern(word):
    punc = string.punctuation
    stri = ""
    for p in punc:
        stri = word.strip()
        stri = word.replace(p,'')
        
    return stri

def sed(filename1,filename2):
     try:
        master = open(filename1,"r")
        unslave = open(filename2,"w")
        for i in master:
            new = removepattern(i)
            unslave.write(i)
        print("File write operation completed successfully :-)")
     except:
        print("Oops something went wrong!!!")


x = input("Enter master file for copy operation:")
y = input("Enter unslave file:")
sed(x,y)
