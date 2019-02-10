import os
list_file=[]
list_dir=[]
def walk(dirname):    
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)        
        if os.path.isfile(path):
            print(path)        
        else:            
            walk(path)
            
walk('/home')
print('list of all files in home or folder')
for i in list_file:
	print(list_file,sep="##",end="")
print()
print('list of all directories')
for i in list_dir:
	print(i[::-1])

walk(os.getcwd())