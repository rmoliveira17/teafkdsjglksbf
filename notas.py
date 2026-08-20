def calculate_mean(numbers):
	"""Return the arithmetic mean of a list of numbers."""
	if not numbers:
		raise ValueError("numbers must not be empty")
	return sum(numbers) / len(numbers)
