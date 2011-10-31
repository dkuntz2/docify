public class javasample {
	
	public static void main(String[] args) {
		System.out.println(factorial(10));
	}

	/**
		Get a factorial *recursively*

		Standard factorial method using recursion, returns 1 if x is less than
		or equal to 1, otherwise it returns `factorial(x-1)`.

		@parameters = [
			x : integer to the the factorial of.
		]

		@returns = [
			defalut : x!
		]
	*/
	public static int factorial(int x) {
		if (x <= 1)
			return 1;
		else
			return factorial(x-1);
	}

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
			default 	: the toJumble String passed in the method header
			
			Case0 	: Nothing, there is no case other than the standard one
		]
	*/
	public String jumble(String toJumble, int numTimes) {
		return toJumble;
	}
}