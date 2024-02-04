import sys

class SeqDetectEngine: 

	bInitOK = False
	bInDebug = False
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
		print("countDigits() Not yet implemented")
		
	def isSequence(self, inNum): 
		print("isSequence() Not yet implemented")

	def go(self):
		print("go() Not yet implemented")

	def debugMsg(self, msg): 
		if (self.bInDebug):
			print(msg)
	
