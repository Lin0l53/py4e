#partner was Logan Zipp
fname = "mbox-short.txt"
handle = open(fname) 
counter = dict()
for line in handle :
	if line.startswith("From ")  :
		line = line.rstrip()
		#print (line)
		words = line.split()
		sender = words[2]
		counter[sender] = counter.get(sender,0) + 1
		
			

print (counter)