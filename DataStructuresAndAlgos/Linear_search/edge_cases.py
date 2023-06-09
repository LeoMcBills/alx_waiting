#!/usr/bin/python3
import json

cases = {
			'case1' : {
						'cards' : [],
						'choice': 3
					},

			'case2' : {
						'cards' : [1, 2, 3, 6, 6, 6, 7, 6],
						'choice': 6
					},

			'case3' : {
						'cards' : [4, 6, 7, 3, 2],
						'choice': 1
					},

			'case4' : {
						'cards' : [0, 6, 9, 3],
						'choice': 0
					},

			'case5' : {
						'cards' : [4, 3, 2, 5, 4],
						'choice': 4
					}
		}

print(json.dumps(cases, sort_keys=True, indent=4))
