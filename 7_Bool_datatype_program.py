# 1)bool(0)  False
# 2) bool(1)  True
# 3) bool(10)  True
# 4) bool(10.5)  True
# 5) bool(0.178)  True
# 6) bool(0.0)  False
# 7) bool(10-2j)  True
# 8) bool(0+1.5j)  True
# 9) bool(0+0j)  False
# 10) bool("True")  True
# 11) bool("False")  True
# 12) bool("")  False

# ************** INT DATATYPE *******************

# 0 ----> False
# 1------> True
print("***** Int data type to bool ")
print(bool(0))
print(bool(1))
# ************** FLOAT DATATYPE *******************
print("***** FLOAT data type to bool ")
print(bool(0.0))
print(bool(1.256))
# O.0 ----> False
# Other than that------> True

# ************** Complex DATATYPE *******************
print("***** Complex data type to bool ")
print(bool(0+0j))
print(bool(0+1j))
# 0+0j ----> False
# other that that ------> True

# ************** STRING DATATYPE *******************
print("***** STRING data type to bool ")
print(bool(""))
print(bool("c"))
# Empty----> False
# Other than that------> True

