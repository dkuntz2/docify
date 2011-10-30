# javadocify - as implemented in python?

from sys import argv
import re

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
		
	print "out of tabs"

	pathList = f.split("/")
	fname = pathList[len(pathList) - 1]


	writer = open(fname.replace(".java", ".md"), "w")
	for b in blocks:
		numTabs = 0;

		tmpInt = b.index("\n")

		tmp = b[0:int(tmpInt)]

		moreTabs = True

		while moreTabs:
			try :
				if tmp.index("\t") == 0:
					numTabs += 1
					tmp = tmp[1:len(tmp)]
			except ValueError:
				moreTabs = False
		
		b = "\n" + b

		# grab the $parameters block area
		param = []
		para = re.search('@parameters\s=\s\[[^\]]*', b)
		
		paramStr = para.group();
		paramStart = re.search('@parameters\s=\s\[', paramStr)
		paramStr = paramStr[paramStart.span()[1]:len(paramStr)].replace("\n" + ("\t" * (numTabs + 1)), "\n")

		# grab the @return block area
		retur = []
		ret = re.search('@returns\s=\s\[[^\]]*', b)

		retStr = ret.group()
		retStart = re.search('@returns\s=\s\[', retStr)
		retStr = retStr[retStart.span()[1]:len(retStr)].replace("\n" + ("\t" * (numTabs + 1)), "\n")


		# set b to everything before the parameters
		b = b[0:para.span()[0]]
		# remove returns block from b
		b = b[0:ret.span()[0]]

		# write out the docify block
		writer.write(b.replace("\n" + ("\t" * numTabs), "\n"))

		# parameters
		writer.write("#### Parameters\n")
		writer.write(paramStr)

		# returns
		writer.write("\n\n#### Returns\n")
		writer.write(retStr)

		# separater
		writer.write("\n========\n")
	