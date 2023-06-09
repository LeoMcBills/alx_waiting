#!/usr/bin/python3
import json

def use_case(case: str)->dict:
	"""A dict of all possible testing edge cases

	Parameter
	----------
	case: (str)
		Enter the name of the case to test the algorithm with

	Returns
	-------
	A dictionary of the particular test edge case
	"""

	cases = {
				'case_1' : {
							'cards' : [],
							'choice': 3
						},
	
				'case_2' : {
							'cards' : [1, 2, 3, 6, 6, 6, 7, 6],
							'choice': 6
						},
	
				'case_3' : {
							'cards' : [4, 6, 7, 3, 2],
							'choice': 1
						},
	
				'case_4' : {
							'cards' : [0, 6, 9, 3],
							'choice': 0
						},
	
				'case_5' : {
							'cards' : [4, 3, 2, 5, 4],
							'choice': 4
						}
		}
	for key, value in cases.items():
			print(key, "contains ", value)
			print()


# print(use_case('case3'))
use_case('case1')
