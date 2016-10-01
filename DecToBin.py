
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
DecToBin()
