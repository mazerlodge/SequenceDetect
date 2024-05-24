import sys

class SeqDetectEngine: 

	bInitOK = False
	bInDebug = False
	rawNumber = 0

	def __init__(self, args): 
		self.parseArgs(args)


	def parseArgs(self, args):
		self.bInitOK = False 

		argCount = len(args)
		self.debugMsg(f"Arg Count = {argCount}") 

		if (argCount >= 2):
			self.rawNumber = int(args[1])
			self.bInitOK = True

		if ((argCount >= 3) and (args[2].lower() == "-debug")):
			self.bInDebug = True

		if (self.bInDebug):
			for x in range(0,argCount):
				self.debugMsg(f"arg[{x}] = {args[x]}")


	def showUsage(self):
		print("Usage: SeqDetect 456 [-debug] (returns True).\nSeqDetect 457 (returns False)")


	def countDigits(self, inNum):
		return len(str(inNum))


	def makeArrayOfDigits(self, fromNum):
		digitArray = []
		numLength = self.countDigits(fromNum)

		self.debugMsg(f"Your number {fromNum} has {numLength} digits")

		# put the digits of the input number into an array 
		workingNum = fromNum
		for currentDigIdx in range(numLength-1, 0, -1):
			denom = 10 ** currentDigIdx
			currentDigit = workingNum // denom 
			digitArray.append(currentDigit)
			workingNum = workingNum - (currentDigit * denom) 

		# add the last digit to the array
		digitArray.append(workingNum)

		return(digitArray)


	def isSequence(self, inNum): 
		bIsSequence = True
		digitArray = self.makeArrayOfDigits(inNum)

		# Walk digits, right to left, seeing if the val is 1 less than prev val
		adjustedVal = digitArray[len(digitArray)-1]
		for x in range(len(digitArray)-1, -1, -1):
			if (digitArray[x] != adjustedVal):
				bIsSequence = False
				break
			adjustedVal = adjustedVal - 1

		return(bIsSequence)


	def isOutOfOrderSequence(self, inNum): 
		bIsSequence = True

		# Sort the numbers 
		digitArray = self.makeArrayOfDigits(inNum)
		digitArray.sort()

		# Walk digits, right to left, seeing if the val is 1 less than prev val
		adjustedVal = digitArray[len(digitArray)-1]
		for x in range(len(digitArray)-1, -1, -1):
			if (digitArray[x] != adjustedVal):
				bIsSequence = False
				break
			adjustedVal = adjustedVal - 1

		return(bIsSequence)


	def go(self):
		if (self.isSequence(self.rawNumber)):
			print(f"Your number {self.rawNumber} is a sequence.")
		else:
			if (self.isOutOfOrderSequence(self.rawNumber)):
				print(f"Your number {self.rawNumber} is an out of order sequence.")
			else:
				print(f"Your number {self.rawNumber} is not a sequence.")


	def debugMsg(self, msg): 
		if (self.bInDebug):
			print(msg)

