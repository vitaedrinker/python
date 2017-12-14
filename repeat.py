# Compare two lines of a text file and look for repeats

import datetime
import unicodedata

print("All files must be .txt files.")
name = input("What is the file name? ")+".txt"
outputname = input("What would you like to call the output?")+".txt"
now = datetime.datetime.now().strftime("%Y-%m-%d "".txt")
type(name)

lines_seen = set() 														# holds lines already seen
outfile = open(now, "w+")
for line in open (name, "r", encoding='utf-8'):
	if line not in lines_seen:											# not a duplicate
		outfile.write(line)
		lines_seen.add(line)
outfile.close()
