#Binary to Decimal
#By ImOverlord


def main():
	bin = raw_input("Enter Binary: ")
	binLen = len(bin)

	#Check if input is Binary
	for i in range(binLen):
	        
	        if not bin[i] in ["1","0"]:
	                print "Error, Input entered not in binary"
	                main()


	#VARs
	x = binLen
	y = 0
	z = ""

	print ' '.join(["\nConverting",bin,"to decimal\n"])

	#Convertion Code
	for i in range(binLen):
		
		y = y + (int(bin[i])*pow(2,binLen))/2
		
		binLen = binLen - 1


	a = str(y)
	print ' '.join([bin,"is",a,"in decimal"])
	exit() #EXT

main()