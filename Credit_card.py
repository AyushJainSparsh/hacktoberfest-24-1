class CreditCard:
	@staticmethod
	def main(args):
		number = 5196081888500645
		print(str(number) + " is " +
			("valid" if CreditCard.isValid(number) else "invalid"))
		
	@staticmethod
	def isValid(number):
		return (CreditCard.getSize(number) >= 13 and CreditCard.getSize(number) <= 16) and (CreditCard.prefixMatched(number, 4) or CreditCard.prefixMatched(number, 5) or CreditCard.prefixMatched(number, 37) or CreditCard.prefixMatched(number, 6)) and ((CreditCard.sumOfDoubleEvenPlace(number) + CreditCard.sumOfOddPlace(number)) % 10 == 0)
	
	@staticmethod
	def sumOfDoubleEvenPlace(number):
		sum = 0
		num = str(number) + ""
		i = CreditCard.getSize(number) - 2
		while (i >= 0):
			sum += CreditCard.getDigit(int(str(num[i]) + "") * 2)
			i -= 2
		return sum

	@staticmethod
	def getDigit(number):
		if (number < 9):
			return number
		return int(number / 10) + number % 10
	
	@staticmethod
	def sumOfOddPlace(number):
		sum = 0
		num = str(number) + ""
		i = CreditCard.getSize(number) - 1
		while (i >= 0):
			sum += int(str(num[i]) + "")
			i -= 2
		return sum
	
	@staticmethod
	def prefixMatched(number, d):
		return CreditCard.getPrefix(number, CreditCard.getSize(d)) == d
    
	@staticmethod
	def getSize(d):
		num = str(d) + ""
		return len(num)
    
	@staticmethod
	def getPrefix(number, k):
		if (CreditCard.getSize(number) > k):
			num = str(number) + ""
			return int(num[0:k])
		return number

if __name__ == "__main__":
	CreditCard.main([])
