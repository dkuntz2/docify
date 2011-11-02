'''/**
	Get a factorial *recursively*

	Standard factorial method using recursion, returns 1 if x is less than
	or equal to 1, otherwise it returns `factorial(x-1)`.

	@parameters = [
		x : integer to the the factorial of.
	]

	@returns = [
		default : x!
	]
*/'''
def factorial(x=5):
	if x <= 1:
		return 1
	else :
		return x * factorial(x - 1)

