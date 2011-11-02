import re

'''/**
	Get a list of files from a list that use the extension.

	@parameters = [
		files: array of file paths, generally received from the argv

		extension: extension of files you want. Does not contain the preceding period.
		If you want all .py files, send "py" as your extension.
	]

	@returns = [
		default: list of files that are indeed the right extension.
	]
*/'''
def getFiles(files, extension):
	return getFiles(files, extension, "")

'''/**
	Get a list of files from a list that use the extension, but don't include a
	certain file.

	@parameters = [
		files: array of file paths, generally received from the argv

		extension: extension of files you want. Does not contain the preceding period.
		If you want all .py files, send "py" as your extension.

		excludeFile: the full name of the file you want to exclude, generally
		the name of the file being called if you use `argv` for your files array.
		This is useful when your extension is `py`, because you can tell the
		script to NOT look at itself. Always useful.
	]

	@returns = [
		default: list of files that are indeed the right extension.
	]
*/'''
def getFiles(files, extension, excludeFile):
	files = []
	for f in files:
		slah = f.split('/')
		if slah[len(slah) - 1] != excludeFile :
			s = f.split(".")
			if len(s) > 1 and s[len(s) - 1] == extension:
				files.append(f)
			
	return files

'''/**
	Get the docify block, using the default docify block declarations `/**` to start
	and `*/` to stop, also assuming that the method starts with `{`.

	@parameters = [
		file: The file you're going to grab the docify blocks from.
	]

	@returns = [
		default: A list of unparsed docify blocks.
	]
*/'''
def grabDocifyBlock(file) :
	return grabDocifyBlock(file, "/**", "*/", "{")

'''/**
	Get the docify block, using custom start and stop declarations.

	@parameters = [
		file: The file you're going to grab the docify blocks from.

		start: The pattern for the start of a docify block.

		stop: The patter for the end of a docify block.

		methodStart: The character used to start the method, in Java it's `{`,
		in Python it's `:`.
	]

	@returns = [
		default: A list of unparsed docify blocks.
	]
*/'''
def grabDocifyBlock(file, start, stop, methodStart) :
	blocks = []
	f = open(f)

	text = ""
	for line in f:
		text += line
	
	t = text.split(start)
	t.pop(0)

	unparsed = []
	for e in t:
		tmpBlock = e.split(stop)
		tmpMethStart = tmpBlock[1].split(methodStart)
		unparsed.append(tmpBlock[0] + "\n\n" + tmpMethStart[0].replace("\t" * (numTabs - 1), ""))
	
	for b in unparsed:
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
		blocks.append(b.replace("\n" + ("\t" * numTabs), "\n"))

	return blocks

'''/**
	Get a parameter block, formatted as:

		## Parameters

		### param1

		What it does

		...
	
	it should work real nice like.

	@parameters = [
		block: The docify block to get the parameters from, including the
		method header (which is kept intat if you ues the `grabDocifyBlock`
		method).
	]

	@returns = [
		default: A string of the parameters parsed from the block
	]
*/'''
def getParams(block):
	para = re.search('@parameters\s=\s\[[^\]]*', block)


	out = "## Parameters\n"

	if para != None :
		paramStr = para.group()
		paramStart = re.search('@parameters\s=\s\[', paramStr)
		paramStr = paramStr[paramStart.span()[1]:len(paramStr)]

		tmpPara = paramStr.split("\n\n")
		for t in tmpPara:
			varName = re.search('[^:]*', t)
			varVal = re.search('\s[^:]*', t[varName.span()[1]:len(t)]).group()
			varName = varName.group().replace(" ", "").replace("\n", "")
			out += "\n### " + varName
			out += "\n\n" + varVal + "\n"

	return out


def getReturn(bloc):
	

