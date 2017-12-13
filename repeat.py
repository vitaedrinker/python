# Compare two lines of a text file and look for repeats

import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d Phishing URLs.txt")
name = input("What is the file name? ")+".txt"
type(name)

lines_seen = set() 														# holds lines already seen
outfile = open(now, "w+")
for line in open (name, "r"):
	if line not in lines_seen:											# not a duplicate
		outfile.write(line)
		lines_seen.add(line)
outfile.close()
