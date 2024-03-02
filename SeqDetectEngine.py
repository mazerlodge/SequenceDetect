import sys

class SeqDetectEngine: 

	bInitOK = False
	bInDebug = True
	rawNumber = 0

	def __init__(self, args): 
		self.parseArgs(args)

	def parseArgs(self, args):
		argCount = len(args)
		self.debugMsg(f"Arg Count = {argCount}") 
		
		if (argCount >= 2):
			self.rawNumber = int(args[1])
			self.bInitOK = True

			# Debug use only
			if (self.bInDebug):
				for x in range(0,argCount):
					self.debugMsg(f"arg[{x}] = {args[x]}")

		else:
			self.bInitOK = False 

	def showUsage(self):
		print("Usage: SeqDetect 456 (returns True).\nSeqDetect 457 (returns False)")
	
	def countDigits(self, inNum):
		return len(str(inNum))
		
	def isSequence(self, inNum): 
		numLength = self.countDigits(self.rawNumber)
		print(f"Your number {self.rawNumber} has {numLength} digits")
		digitArray = []


		workingNum = self.rawNumber
		for currentDigIdx in range(numLength-1, 0, -1):
			denom = 10 ** currentDigIdx
			currentDigit = workingNum // denom 
			digitArray.append(currentDigit)
			workingNum = workingNum - (currentDigit * denom) 

		digitArray.append(workingNum)

		for aDig in digitArray:
				print(aDig)

	def go(self):
		self.isSequence(self.rawNumber)

			

	def debugMsg(self, msg): 
		if (self.bInDebug):
			print(msg)
	
