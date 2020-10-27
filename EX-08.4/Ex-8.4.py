#Linus Wiertalla and Logan Yeubanks

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	tempwords =line.rstrip()
	words = tempwords.split()	
	#print(words)
	for word in words:
		if word not in lst :
			#print('s')
			lst.append(word)
lst.sort()
print(lst)

