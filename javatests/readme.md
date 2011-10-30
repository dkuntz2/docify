## Java Tests

This directory is used to hold all of the java tests.

----

30 Oct:
- 	Started working on a python based parser for java. The system currently finds all 
	docblocks inside of a java file (it checks input files for a .java extension) and
	writes their contents to a file (probably in the same directory as the java file, 
	but I haven't really looked into that yet, I will eventually set it up so that
	it's in the current directory) with the same name, but a markdown extension instead
	of java.