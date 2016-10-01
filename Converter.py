#Binary/Decimal Converter
#By ImOverlord




def DecToBin():
	dec = raw_input("\nEnter Decimal: ")
	for i  in range(len(dec)):
		if not dec[i] in ["0","1","2","3","4","5","6","7","8","9"]:
			print "Error, Input is not a number"
			DecToBin()

	a = dec
	b = 0
	c = 0
	bin = ""
	bin1 = ""
	print ' '.join(['\nConverting', dec, 'to binary\n'])
	while a != 0:
		b = int(a) / 2
		b = int(b)
		c = int(a) - (b * 2)
		a = b
		bin = ''.join([bin,str(c)])
	for i in range(len(bin)):
		s = (len(bin) - 1) - i
		bin1 = ''.join([bin1,bin[s]])
	
	print ' '.join([dec, 'is ',bin1,'in binary'])
	exit()


def BinToDec():
	bin = raw_input("\nEnter Binary: ")
	binLen = len(bin)

	#Check if input is Binary
	for i in range(binLen):
	        
	        if not bin[i] in ["1","0"]:
	                print "Error, Input entered not in binary"
	                BinToDec()

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

def Main():
	print "What Convertion do you want to do? \n \n 1) Binary To Decimal \n 2) Decimal To Binary"
	input1 = raw_input("\n> ")

	if not input1 in ["1","2"]:
		print "Input not recognized\n \n"
		Main()
	elif input1 == "1":
		BinToDec()
	else:
		DecToBin()


Main()