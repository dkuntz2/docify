# javadocify - as implemented in python?

from sys import argv
import re

#files = []
inArr = argv


files = []

for f in inArr:
	s = f.split(".")
	if len(s) > 1:
		if s[len(s) - 1] == "java" :
			files.append(f);


for f in files:
	file = open(f);
	
	text = "";
	for line in file :
		text = text + line


	t = text.split("/**\n");
	t.pop(0)

	blocks = []
	for e in t:
		tmp = e.split("*/");
		tmpStuffs = tmp[1].split("{")
		blocks.append(tmp[0] + "\n\n" + tmpStuffs[0])
	
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
		
		e = "\n" + b

		# grab the $parameters block area
		param = {}
		para = re.search('@parameters\s=\s\[[^\]]*', e)
		
		paramStr = para.group();
		paramStart = re.search('@parameters\s=\s\[', paramStr)
		paramStr = paramStr[paramStart.span()[1]:len(paramStr)].replace("\n" + ("\t" * (numTabs + 1)), "\n")

		# place individual parameters in dict param
		tmpPara = paramStr.split("\n\n")

		for t in tmpPara :
			varName = re.search('[^:]*', t)
			varVal = t[varName.span()[1]:len(t)]
			varVal = re.search('\s[^:]*', varVal).group()
			param[varName.group().replace("\n", "")] = varVal

		# grab the @return block area
		retur = {}
		ret = re.search('@returns\s=\s\[[^\]]*', e)

		retStr = ret.group()
		retStart = re.search('@returns\s=\s\[', retStr)
		retStr = retStr[retStart.span()[1]:len(retStr)].replace("\n" + ("\t" * (numTabs + 1)), "\n")

		tmpRet = retStr.split("\n\n")

		for r in tmpRet:
			caseName = re.search('[^:]*', r)
			caseVal = r[caseName.span()[1]:len(r)]
			caseVal = re.search('\s[^:]*', caseVal).group()
			retur[caseName.group().replace("\n", "")] = caseVal


		# set b to everything before the parameters
		e = e[0:para.span()[0]]
		# remove returns block from b
		e = e[0:ret.span()[0]]

		# Get fun method stuff
		methodHeader = b.split("\n\n")[len(b.split("\n\n")) - 1]
		methodHeader = methodHeader.replace("\n" + ("\t" * (numTabs - 1)), "")

		#public or private
		pubpriv = ("public" if methodHeader.index("public") == 0 else "private")
		
		# is it static
		static = False
		try :
			static = True if methodHeader.index("static") > -1 else False
		except ValueError :
			static = False

		# return type
		numCharsBefore = len(pubpriv) + 1
		if static :
			numCharsBefore += 7
		retType = methodHeader[numCharsBefore:len(methodHeader)].split(" ")[0]
		
		# methodName
		numCharsBefore += len(retType) + 1
		methodName = methodHeader[numCharsBefore:len(methodHeader)].split("(")[0]

		# write method name and other fun stuff
		writer.write("# " + pubpriv + (" static " if static else " ") + methodName + "\n")

		# write out the docify block
		writer.write(e.replace("\n" + ("\t" * numTabs), "\n"))

		# parameters
		writer.write("## Parameters\n")
		for k in param:
			writer.write("\n### " + k + "\n\n" + param[k][1:len(param[k])] + "\n")

		# returns
		writer.write("\n## Returns - " + retType + "\n")
		for k in retur:
			writer.write("### " + k + "\n\n" + retur[k][1:len(retur[k])] + "\n")
		
		#writer.write(b.split("\n\n")[len(b.split("\n\n")) - 1])
		# separater
		if blocks.index(b) < len(blocks) - 1:
			writer.write("\n-----\n")
	