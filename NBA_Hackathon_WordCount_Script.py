# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 21:46:18 2018

@author: Xingyuan Gu, Peter Law
"""
#coding:utf-8
def read_file():
	f=open('C:/Users/dell/.spyder-py3/WordTesting.txt',encoding='ISO-8859-1')
	readline=f.readlines()
	word=[]
 
	for line in readline:
		line=line.replace(',','').replace('-','').replace('&','').replace('vs','').replace('vs.','').replace('VS','').replace('+','').replace('.','') 
		line=line.strip()
		wo=line.split(' ')
		word.extend(wo)
	return word

def clear_account(lists):
	wokey={}
	wokey=wokey.fromkeys(lists)
 
	word_1=list(wokey.keys())
	for i in word_1:
		wokey[i]=lists.count(i)
	return wokey

def sort_1(wokey):
	del[wokey['']]
	wokey_1={}
	wokey_1=sorted(wokey.items(),key=lambda d:d[1],reverse=True)
	wokey_1=dict(wokey_1)
	return wokey_1

def main(wokey_1):
	i=0
	for x,y in wokey_1.items():
		if i<50:
			print('the word is "','{}'.format(x),'"',' and its amount is "','{}'.format(y),'"')
			i+=1
			continue
		else:
			break
main(sort_1(clear_account(read_file())))






