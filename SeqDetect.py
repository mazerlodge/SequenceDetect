import sys
from SeqDetectEngine import SeqDetectEngine

sde = SeqDetectEngine(sys.argv)

if (not sde.bInitOK):
	sde.showUsage()
	sys.exit()
else:
	sde.go()
