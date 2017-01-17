def generate_primes(n):
	if n < 2:
		raise ValueError("Wrong Value")

	if not isinstance(n, int):
		raise TypeError("Wrong")

	primes = []
	for num in range (2, n + 1):
		isPrime = True
		for x in range (2, num):
			if num % x == 0:
				isPrime = False
		if isPrime:
			primes.append(num)

	return primes


if __name__ == '__main__':
	print(generate_primes(5))
	print(generate_primes(1))