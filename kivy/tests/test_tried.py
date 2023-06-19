import unittest

class OnTestCase(unittest.TestCase):

	def setUp(self):
		# import class and prepare everything here.
		pass

	def test_input(self):
		# place your test case here
		a = 1
		self.assertEqual(a, 1)

if __name__ == '__main__':
	unittest.main()
