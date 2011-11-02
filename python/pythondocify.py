# javadocify - as implemented in python?

from sys import argv
import re

#files = []
inArr = argv


files = []

for f in inArr:
	slah = f.split('/')
	if slah[len(slah) - 1] != "pythondocify.py" :
		s = f.split(".")
		if len(s) > 1:
			if s[len(s) - 1] == "py":
				files.append(f);


for f in files:
	file = open(f);
	
	text = "";
	for line in file :
		text = text + line


	t = text.split("'''/**\n");
	t.pop(0)

	blocks = []
	for e in t:
		tmp = e.split("*/'''");
		tmpStuffs = tmp[1].split(":")
		blocks.append(tmp[0] + "\n\n" + tmpStuffs[0])
	
	pathList = f.split("/")
	fname = pathList[len(pathList) - 1]


	writer = open(fname.replace(".py", ".md"), "w")
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
		
		# Get fun method stuff
		methodHeader = b.split("\n\n")[len(b.split("\n\n")) - 1]
		methodHeader = methodHeader.replace("\n" + ("\t" * (numTabs - 1)), "")
		
		# methodName
		numCharsBefore = 4;
		methodName = methodHeader[numCharsBefore:len(methodHeader)].split("(")[0]
			
		e = "\n" + b

		# grab the $parameters block area
		paramDes = {}
		param = []
		initparam = []
		para = re.search('@parameters\s=\s\[[^\]]*', e)
		if para != None :
			paramStr = para.group();
			paramStart = re.search('@parameters\s=\s\[', paramStr)
			paramStr = paramStr[paramStart.span()[1]:len(paramStr)].replace("\n" + ("\t" * (numTabs + 1)), "\n")

			# place individual parameters in dict param
			tmpPara = paramStr.split("\n\n")

			paramreg = re.search('([a-zA-Z0-9=\",\ ]+)', methodHeader)
			paramreg2 = re.search('([a-zA-Z0-9=\",\ ]+)', methodHeader.replace(paramreg.group(), ""))
			initvals = paramreg2.group().replace(", ", ",").split(",")
			for iv in initvals :
				tmp = iv.split("=") 
				param.append(tmp[0])
				if len(tmp) >= 2:
					initparam.append(tmp[1])
				else :
					initparam.append("")
				
			for t in tmpPara :
				varName = re.search('[^:]*', t)
				varVal = t[varName.span()[1]:len(t)]
				varName = varName.group().replace(" ", "").replace("\n", "")
				varVal = re.search('\s[^:]*', varVal).group()
				
				paramDes[varName] = varVal
				
		# grab the @return block area
		retur = {}
		ret = re.search('@returns\s=\s\[[^\]]*', e)
		if ret != None :
			retStr = ret.group()
			retStart = re.search('@returns\s=\s\[', retStr)
			retStr = retStr[retStart.span()[1]:len(retStr)].replace("\n" + ("\t" * (numTabs + 1)), "\n")


			tmpRet = retStr.split("\n\n")

			for r in tmpRet:
				caseName = re.search('[^:]*', r)
				caseVal = r[caseName.span()[1]:len(r)]
				caseVal = re.search('\s[^:]*', caseVal).group()
				retur[caseName.group().replace("\n", "")] = caseVal

		

		
		if ret != None :
			# remove returns block from b
			e = e[0:ret.span()[0]]

		if para != None:
			# set b to everything before the parameters
			e = e[0:para.span()[0]]


		# write method name and other fun stuff
		writer.write("# " + methodName + " ( ")
		
		for i in range(len(param)) :
			writer.write(param[i] + (" = " + initparam[i] if initparam[i] != "" else "" ))
			if i < len(param) - 1 :
				writer.write(" , ")		

		writer.write(" )\n")
		# write out the docify block
		writer.write(e.replace("\n" + ("\t" * numTabs), "\n"))

		# parameters
		writer.write("## Parameters\n")
		#for k in param:
		#	writer.write("\n### " + k + "\n\n" + paramDes[k][1:len(paramDes[k])] + "\n")

		for i in range(len(param)) :
			writer.write("\n### " + param[i] + (" = " + initparam[i] if initparam[i] != "" else "" ) + "\n\n"  + (paramDes[param[i]] + "\n" if param[i] in paramDes else "") )

		# returns
		writer.write("\n## Returns\n")
		for k in retur:
			writer.write("### " + k + "\n\n" + retur[k][1:len(retur[k])] + "\n")
		
		#writer.write(b.split("\n\n")[len(b.split("\n\n")) - 1])
		# separater
		if blocks.index(b) < len(blocks) - 1:
			writer.write("-----\n\n")
	