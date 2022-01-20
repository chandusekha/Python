n=int(input("enter the sze ogf triangle...."))
for x in range(1,n+1):
    for y in range(1,x+1):
        print("*",end=' ')
    print()

#   *
#   * *
#   * * *
#   * * * *
#   * * * * *

print("ALTERNATE WAY")

for x in range(1,n+1):
    print("* "*x)