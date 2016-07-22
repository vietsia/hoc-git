
original = raw_input('Enter a word:')
pyg = 'ay'
word=original.lower()
last=word[(len(word)-1):len(word)]
midle=word[0:(len(word)-1)]
new_word=last+midle+pyg
if len(original) > 0 and original.isalpha()==True:
    	print new_word
    	print last
elif len(original)>0 and original.isalpha()==False:
	print 'ban da nhap sai, moi nhap word'
                 
else:
    	print 'empty'
