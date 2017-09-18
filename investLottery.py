# (c) 2017 TrueFlip S.A.R.L
# usage python investLottery.py 000000000000000000b3dc58aa1fbbba543186a8154a51460b0a75ddde8da9cf 50
import sys

def getWinner(seed,N):
	print("Seed is: " + seed[-12:])
	print("Number is: " + str(long(seed[-12:],16)))
	intRep = divmod(int(seed[-12:],16),N)[1]
	if intRep == 0:
		return N
	else:
		return intRep


if __name__ == '__main__':
	seed = sys.argv[1]
	N = sys.argv[2]
	print(getWinner(seed,int(N)))	


