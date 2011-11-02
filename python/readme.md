# Docify for Python

## Specifications (alpha 1)

Due to Python's use of the tripple single quote (`'''`) for multi-line comments, 
Python gets a slightly modified version of the original [Java specifications](../java/readme.md).

To start off a docify block in Python, start with the standard multi-line comment,
and, on the same line add the slash-star-star (`/**`) that is standard in most other 
languages.

	'''/**

And to finish off a docify block in Python, just use:

	*/'''

All on the same line. The if the docblock starters and stoppers are not kept of the same
line as the beginning of the initial comment starter, it will not work.

Additionally, all lines following 

----

The following is a basic docify block for a simple method:

	'''/**
		Jumble up a string

		Currently it doesn't do anything, as the whole method is

			def jumble(toJumble="", numTimes=5) :
				return toJumble;
			
		However in the possible future, it might do something, something
		really cool like. YEAH.

		@parameters = [
			toJumble: The word to jumble up.

			numtimes: The number of times to jumble the word.
		]

		@returns = [
			default: toJumble, that's it right now.
		]
	/*'''
	def jumble(toJumble="", numTimes=5) :
		return toJumble;
	
Based off of that docify block, you would get the following in return:

# jumble ( toJumble = "", numTimes = 5 )

Jumble up a string

Currently it doesn't do anything, as the whole method is

	def jumble(toJumble="", numTimes=5) :
		return toJumble;

However in the possible future, it might do something, something
really cool like. YEAH.

## Parameters

### toJumble = ""

The word to jumble up.

### numTimes = 5

The number of times to jumble the word.
		

## Returns - String
### default 	

the toJumble String passed in the method header