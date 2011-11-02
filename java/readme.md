# Docify for Java

## Specifications (alpha 1)

To start off a docify block, use the slash-star-star, like javadoc

	/**

To end a docify block, just close the multi-line comment
	
	*/

Docify, unlike javadoc does not require a star for each line, just that new lines be used
for separators. Additionally, docify uses 
[markdown](http://daringfireball.net/projects/markdown) for styling comments.

You must have each line of a docify block one tab in compared to the starting and 
ending characters, as seen below. If you keep everything at the same level, docify will
not work.

--------

The following is a basic docify block for a simple method:

	/**
		Jumble up a string

		Currently it doesn't do anything, as the whole method is

			public static String jumble(String toJumble, int numTimes) {
				return toJumble;
			}

		However in the possible future, it might do something, something
		really cool like. YEAH.

		@parameters	= [
			toJumble: The word to jumble up
			
			numTimes: The number of times to jumble the word
		]

		@returns	= [
			Case0 	: Nothing, there is no case other than the standard one

			default 	: the toJumble String passed in the method header
		]
	*/
	public static String jumble(String toJumble, int numTimes) {
		return toJumble;
	}

Docify would generate the following based off of that block:

# public jumble ( String toJumble, int numTimes )

Jumble up a string

Currently it doesn't do anything, as the whole method is

	public static String jumble(String toJumble, int numTimes) {
		return toJumble;
	}

However in the possible future, it might do something, something
really cool like. YEAH.

## Parameters

### toJumble - String

The word to jumble up

### numTimes - int

The number of times to jumble the word
		

## Returns - String
### Case0 	

Nothing, there is no case other than the standard one
		
### default 	

the toJumble String passed in the method header

## Notes

Docify is not yet complete, and as such, it does not create documentation in that format
yet. This document is only meant to show how docify will work in the future.