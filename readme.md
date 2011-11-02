# Modular Docify

This is the Modular branch of Docify, where we're trying to make docify more modular 
in nature, so that people who want to can hop in and grab exactly what they need to
make their own implementation of Docify, or even just use some code that's already
been written before instead of writing their own.

Right now this is really developmenty, and you probably shouldn't use it unless you're
looking at helping make it less developmenty...

# Docify

Docify is a (currently hypothetical) alternative documentation markup reader/creator.

Docify will be made available for multiple programming languages, however the first
language to receive a Docify tool will most likely be Java or Python.

Docify will use markdown inside of multi-line comments as opposed to html (as is the
case with javadoc).


## Paths Scheme

All tests will take place in the tests branch, when a test is determined to be ready
for general use, it will be placed in the master branch.

A tests directory will reside in each language name directory, it will contain a file
with the language's docify specifications inside of it as well as the output from docify.