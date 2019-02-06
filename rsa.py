import math
import random

def calculateE(p,q,phi):
	list1 = []
	for e in range(2,phi):
		if math.gcd(e,phi) == 1:
			list1.append(e)
	return list1

def calculateD(phi,e):
	for d in range(1,phi):
		if (d*e)%phi is 1:
			return d

def charalgo():
	p = int(input("Enter the first prime number:"))
	q = int(input("Enter the second prime number:"))
	n=p*q
	phi = (p-1)*(q-1)
	list1 = calculateE(p,q,phi)
	print(list1)
	e = random.choice(list1)
	print("e = "+ str(e))
	d = calculateD(phi,e)
	print("d = " +str(d))
	print("Public key is (n="+str(n)+",e="+str(e)+")")
	print("Private key is (n="+str(n)+",d="+str(d)+")")
	print("--------------------")
	pt = input("Enter text data: ")
	print("Encrypting...")
	enc = []
	dec = []
	for i in pt:
		c = (ord(i)**e)%n
		enc.append(c)
	print(enc)
	print("--------------------")
	print("Decrypting...")
	for j in enc:
		m = (j**d)%n
		dec.append(chr(m))
	str1 = ''.join(dec)
	print(str1)



def algo():
	p = int(input("Enter the first prime number:"))
	q = int(input("Enter the second prime number:"))
	n=p*q
	phi = (p-1)*(q-1)
	list1 = calculateE(p,q,phi)
	print(list1)
	e = random.choice(list1)
	print("e = "+ str(e))
	d = calculateD(phi,e)
	print("d = " +str(d))
	print("Public key is (n="+str(n)+",e="+str(e)+")")
	print("Private key is (n="+str(n)+",d="+str(d)+")")
	print("--------------------")
	data = int(input("Enter data (numerical data only): "))
	print("Encrypting...")
	c = (data**e)%n
	print("Encrpyted data : "+str(c))
	print("--------------------")
	print("Decrypting...")
	dec = (c**d)%n
	print("Decrypted data :"+str(dec))

charalgo()
