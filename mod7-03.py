#Partner is Cameron
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
	if fname == "na na boo boo":
		print ("NA NA BOO BOO TO YOU - You have been punk'd")
	else:
		print("File cannot be opened :",fname)
	quit()
totalcount = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    cline = line.find(":")
    cdata = line[cline+1:]
    fdata = float(cdata.lstrip())
    #print(fdata)
    count = count + 1
    totalcount = fdata + totalcount

#print(count)
#print(totalcount)
print("Average spam confidence:",totalcount/count)
#print("Done")
