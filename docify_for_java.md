# Docify for Java

## Specifications (alpha 1)

To start off a docify block, use the slash-star-star, like javadoc

	/**

To end a docify block, just close the multi-line comment
	
	*/

Docify, unlike javadoc does not require a star for each line, just that new lines be used
for separators. Additionally, docify uses 
[markdown](http://daringfireball.net/projects/markdown) for styling comments.

--------

The following is a basic docify block for a recursive factorial method:

	/**
		Get a factorial *recursively*.

		Standard factorial method using recursion, returns
		1 if x is less than or equal to 1, otherwise it returns
		`factorial(x-1)`.

		@param 	x	integer to get the factorial of.
		@return	x!

	*/
	public int factorial(int x) {
		if (x <= 1)
			return 1;
		else
			return foo(x - 1);
	}

Docify would generate the following based off of that block:

### factorial( int x )

Get a factorial *recursively*

Standard factorial method using recursion, returns 1 if x is less than or equal to 1, 
otherwise it returns `factorial(x-1)`.

#### Parameters

- **int x** - integer to get the factorial of.

#### Returns

x!