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