import string
import matplotlib.pyplot as pyplot
import math
from operator import itemgetter
book_list=[]
book_dict={}
def word_histo(word):
	global dic


def depunctuate(line):
	for repl in string.punctuation:
		line=line.replace(repl, " ")
	return line
def read(file):
	dic={}
	fout=open(file,'r')
	for line in fout:
		line=line.strip(string.whitespace+string.punctuation)
		line=depunctuate(line)
		for i in line.split():
			dic[i]=dic.get(i,0)+1
	return dic

book_dict=read('cobb.txt')

book_list=[(values,keys) for keys,values in sorted(book_dict.items())]
book_list=sorted(book_list,reverse=True)
pyplot.clf()
pyplot.xscale('log')
pyplot.yscale('log')
pyplot.title('The Zipf graph')
pyplot.xlabel('Rank')
pyplot.ylabel('frequency')
for rank in range(2,len(book_list)):
	pyplot.plot(rank,rank)
pyplot.show()