import unittest

#Imports the function generate_primes from the generatePrimesFunction function file
from generatePrimesFunction import generate_primes


class TestFunctionInputs(unittest.TestCase):

	def test_input_type(self):
		with self.assertRaises(TypeError):
			generate_primes("Hello")

	def test_valid_input(self):
		self.assertEqual(generate_primes(5), [2, 3, 5])

	def test_invalid_input(self):
		with self.assertRaises(ValueError):
			generate_primes(-1)

	def test_input_zero(self):
		with self.assertRaises(ValueError):
			generate_primes(0)



class TestFunctionOutputs(unittest.TestCase):

	def test_output_type(self):
		self.assertIsInstance(generate_primes(3), list)

	def test_valid_output(self):
		self.assertIn(2, generate_primes(5))

	def test_output_size(self):
		self.assertEqual(len(generate_primes(5)), 3)

	def test_one_as_input(self):
		with self.assertRaises(ValueError):
			generate_primes(1)


if __name__ == '__main__':
	unittest.main()
