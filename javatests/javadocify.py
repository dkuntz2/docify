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

	t = text.split("/**\n");
	t.pop(0)

	blocks = []
	for e in t:
		tmp = e.split("*/");
		blocks.append(tmp[0])
	
	# determine initial tab push, will be basis for all following ones...
	numTabs = 0;

	tmpInt = blocks[0].index("\n")

	tmp = blocks[0][0:int(tmpInt)]

	moreTabs = True

	while moreTabs:
		try :
			if tmp.index("\t") == 0:
				numTabs += 1
				tmp = tmp[1:len(tmp)]
		except ValueError:
			moreTabs = False
		
	print "out of tabs"

	writer = open(f.replace(".java", ".md"), "w")
	for b in blocks:
		b = "\n" + b
		writer.write(b.replace("\n" + ("\t" * numTabs), "\n"))
	