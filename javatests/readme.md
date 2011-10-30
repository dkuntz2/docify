## Java Tests

This directory is used to hold all of the java tests.

----

30 Oct:

1. 	Started working on a python based parser for java. The system currently finds all 
	docblocks inside of a java file (it checks input files for a .java extension) and
	writes their contents to a file (probably in the same directory as the java file, 
	but I haven't really looked into that yet, I will eventually set it up so that
	it's in the current directory) with the same name, but a markdown extension instead
	of java.

2.	Figured out how many tabs there are on the initial line, the system now knows to 
	replace the beginning tabs (provided they aren't extra indentations for a code
	block, those *should* remain intact). Markdown still not parsed. Also, it only prints
	the first docblock section... Need to fix that.

3.	Okay, now it accepts multiple docblocks, which is fun. They're currently delineated 
	with `========`, just for my own convenience. But hey, that's cool, next up: getting
	the @param and @return working, because that will be really cool (also getting the
	method name, that'd be fun too).

4.	Instead of figuring out the @ stuff, I fixed the abs path problem. The system used to
	create the markdown document in same directory as the java file being docified, now
	it's created in the working directory (calling `python javatests/javadocify.py javatests/*.java` creates the markdown files in the root, not inside of javatests,
	like how javadoc does).

5.	Okay, lots of updates between previous notes, BUT, the system now has fun time with 
	the docblock, and displays most of the things you want to see, in a somewhat useful
	format. I still need to get the method header, but that shouldn't be that hard...