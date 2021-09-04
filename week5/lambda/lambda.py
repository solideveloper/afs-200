def mult (y) :
     return lambda x : x * y

x = mult(7)
print(x(12))