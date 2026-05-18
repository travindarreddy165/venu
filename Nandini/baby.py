def check_even_odd(number):
	if number % 2 == 0:
		return "even"
	return "odd"


if __name__ == "__main__":
	numbers = list(range(1, 21))
	for num in numbers:
		result = check_even_odd(num)
		print(f"{num} is {result}")
