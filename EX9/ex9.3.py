#partner was Logan Zipp
fname = "mbox-short.txt"
handle = open(fname) 
counter = dict()
for line in handle :
	if line.startswith("From:")  :
		line = line.rstrip()
		print (line)
		words = line.split()
		sender = words[1]
		counter[sender] = counter.get(sender,0) + 1
		
			

max = -1
word = None
for m,c in counter.items() :
	if c > max :
		max = c
		word = m
		
print(counter)
#print (words)
#print (sender)
#print (counter)