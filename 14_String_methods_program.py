# We can use the following 3 methods
# 1) rstrip()  To remove spaces at right hand side
# 2) lstrip() To remove spaces at left hand side
# 3) strip()  To remove spaces both sides


city=input("Enter your city Name:")
scity=city.strip()
if scity=='Hyderabad':
    print("Hello Hyderbadi..Adab")
elif scity=='Chennai':
    print("Hello Madrasi...Vanakkam")
elif scity=="Bangalore":
    print("Hello Kannadiga...Shubhodaya")
else:
    print("your entered city is invalid")

# ***********************************************************************************

# For forward direction:
# 1) find()
# 2) index()
# For backward direction:
# 1) rfind()
# 2) rindex()
#
# s.find(substring)
# Returns index of first occurrence of the given substring. If it is not available then we will get -1.

s="Learning Python is very easy"
print(s.find("Python")) #9
print(s.find("Pava")) # -1
print(s.find("r"))#3
print(s.rfind("r",20,25))#21


# index():
# index() method is exactly same as find() method except that if the specified substring is
# not available then we will get ValueError.
s=input("Enter main string:")
subs=input("Enter sub string:")
try:
    n=s.index(subs)
except ValueError:
    print("substring not found")
else:
    print("substring found")

# Counting substring in the given String:
# We can find the number of occurrences of substring present in the given string by using
# count() method.
# 1) s.count(substring)  It will search through out the string.
# 2) s.count(substring, bEgin, end)  It will search from bEgin index to end-1 index

s="abcabcabcabcadda"
print(s.count('a'))
print(s.count('ab'))
print(s.count('a',3,7))

# Replacing a String with another String:
# s.replace(oldstring, newstring)
# inside s, every occurrence of old String will be replaced with new String.
# Eg 1:
s = "Learning Python is very difficult"
s1 = s.replace("difficult","easy")
print(s1)
#
# Splitting of Strings:
#  We can split the given string according to specified seperator by using split() method.
#  l = s.split(seperator)
#  The default seperator is space. The return type of split() method is List.

s="durga software solutions"
l=s.split()
for x in l:
    print(x)

# Joining of Strings:
# We can join a Group of Strings (List OR Tuple) wrt the given Seperator.
# s = seperator.join(group of strings)
# Eg 1:

t = ('sunny', 'bunny', 'chinny')
s = '-'.join(t)
print(s)
#
# Changing Case of a String:
# We can change case of a string by using the following 4 methods.
# 1) upper()  To convert all characters to upper case
# 2) lower()  To convert all characters to lower case
# 3) swapcase()  Converts all lower case characters to upper case and all upper case
# characters to lower case
# 4) title()  To convert all character to title case. i.e first character in every word should
# be upper case and all remaining characters should be in lower case.
# 5) capitalize()  Only first character will be converted to upper case and all remaining
# characters can be converted to lower case

s = 'learning Python is very Easy'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

# To Check Type of Characters Present in a String:
# Python contains the following methods for this purpose.
# 1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
# 2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)
# 3) isdigit(): Returns True if all characters are digits only( 0 to 9)
# 4) islower(): Returns True if all characters are lower case alphabet symbols
# 5) isupper(): Returns True if all characters are upper case aplhabet symbols
# 6) istitle(): Returns True if string is in title case
# 7) isspace(): Returns True if string contains only spaces
# Eg:
print('Durga786'.isalnum())
print('durga786'.isalpha())
print('durga'.isalpha())
print('durga'.isdigit())
print('786786'.isdigit())
print('abc'.islower())
print('Abc'.islower())
print('abc123'.islower())
print('ABC'.isupper())

print('Learning python is Easy'.istitle())
print('Learning Python Is Easy'.istitle())
