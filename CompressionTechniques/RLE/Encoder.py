def dectobinary(dec):
	return hex(dec)[2:]

def binarytodec(binary):
	
	s = str(binary)

	dec = 0
	n = 0

	for c in reversed(s):
		if c == '1':
			dec += pow(2, n)
		
		n += 1

	return dec
	

def encodeRLE(s):
	encoded = []
	count = 1
	i = 0
	c = s[i]

	for i in range(1,len(s)):
		if(s[i] == c):
			count += 1
		else:
			if count >= 3:
				'''
				while count > 127:
					encoded.append([1,127, c])
					count -= 127
				'''
				encoded.append([1, count, c])
			else:
				encoded.append([0,count, c])
			
			c = s[i]
			count = 1
		
		if(i==(len(s)-1)):
			if count >= 3:
				'''
				while count > 127:
					encoded.append([1,127, c])
					count -= 127
				'''
				encoded.append([1, count, c])
			else:
				encoded.append([0,count, c])
	
	i = 0

	while i < len(encoded):
		count = 0
		sen = ''
		while i < len(encoded) and encoded[i][0] == 0:
			count += encoded[i][1]
			sen += encoded[i][2] * encoded[i][1]
			encoded.remove(encoded[i])
		
		if count != 0:
			j = i
			'''
			while count > 127:
				encoded.insert(j, [0, 127, sen[:127]])
				sen = sen[127:]
				count -= 127
				j += 1
			'''
			encoded.insert(j, [0, count, sen])
			i = j

		i+=1
	
	newencode = []
	for temp in encoded:
		newencode.append([temp[0], dectobinary(temp[1]), temp[2]])
	

	return newencode

def decode(encoding):
	s = ''
	for temp in encoding:
		if temp[0] == 1:
			s += temp[2] * binarytodec(temp[1])
		else:
			s += temp[2]

	return s 
