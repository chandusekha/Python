#  When we are dealing with Binary Data we should fix prefix with """"0b""""
# Binary-----0B or ob
# Octal -----0o or 0O
#  Hexa------0x or 0X

a=0b1000
print(a)

b=0b01010111
print(b)

c=0b111
print(c)

#  *****************BASE CONVERSION***********************
print("*****************BASE CONVERSION***********************")

print("*****************BINARY BASE CONVERSION***********************")
print(bin(15))
print(bin(0o1245))
print(bin(0x125))

print("*****************OCTAL BASE CONVERSION***********************")
print(oct(15))
print(oct(0b1101))
print(oct(0x125))

print("*****************HEXA BASE CONVERSION***********************")
print(hex(15))
print(hex(0b1101))
print(hex(0o1257))

# ********** MAIN INFORMATION IN FLOAT DATATYPE*****************
print("******* EXPOIENTAIL DATA ***********")
f=1.2e3
print(f)
