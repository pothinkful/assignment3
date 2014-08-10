import sys
 
def dEO(n1, n2):
	if n1 % n2 == 0:
		return n1 % n2 == 0
	else:
		return False
 
def nfbf(limit):
	for number in range(1, limit+1):
		if dEO(number, 15):
			print "fizz-buzz"
 
		elif dEO(number, 5):
			print "buzz"
 
		elif dEO(number, 3):
			print "fizz"
 
		else:
			print number
 
if __name__ == '__main__':
	if len(sys.argv) != 1:	
		limit = int(sys.argv[1])
	else:
		limit = 100
	nfbf(limit)