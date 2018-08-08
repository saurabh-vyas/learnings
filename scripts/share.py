#!/usr/bin/python

'''
	Weight-age consideration for each Pillar of company
	'Technology' : 35,
	'Network' : 15,
	'Leadership' : 25,
	'Investment' : 25
'''
weights = [[35, 15, 25, 25]]

member = {'Rathish' : 0, 'Saurabh' : 0, 'Raghu' : 0, 'Investor' : 0}				

# Contribution in each consideration for every member
# Order : Rathish, Saurabh, Raghu, Investor				
contribution = [
		 [75, 25, 0, 0],
		 [20, 40, 40, 0],
		 [35, 65, 0, 0],
		 [0, 0, 0, 100]
		]

def calculate_share():
	'''
	  For each team member, multiply the weight assigened to 
	  the contribution that they bring in, and sum of all these
	  will determine the share each member should get.
	'''
	
	# matrix multiplication will do the magic
	result = [[sum(a * b for a, b in zip(X_row, Y_col)) 
				for Y_col in zip(*contribution)] 
				for X_row in weights]
	
	
	member['Rathish'] = result[0][0] / 100.0
	member['Saurabh'] = result[0][1] / 100.0
	member['Raghu'] = result[0][2] / 100.0
	member['Investor'] = result[0][3] / 100.0
	
	for m, s in member.items():
		print('Share for {0} \t: {1}'.format(m, s))

if __name__ == '__main__':
	calculate_share()