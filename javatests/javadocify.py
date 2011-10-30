# javadocify - as implemented in python?

from sys import argv

#files = []
inArr = argv

#print "File: ", files[1]

files = []

for f in inArr:
	s = f.split(".")
	if len(s) > 1:
		if s[len(s) - 1] == "java" :
			#print "File: " + f
			files.append(f);

print "\n==========\n"

for f in files:
	print "File: " + f

	file = open(f);
	print file;

	text = "";
	for line in file :
		text = text + line

	#print text

	t = text.split("/**");
	t.pop(0)

	blocks = []
	for e in t:
		tmp = e.split("*/");
		blocks.append(tmp[0])

	writer = open(f.replace(".java", ".md"), "w")
	for b in blocks:
		writer.write(b)