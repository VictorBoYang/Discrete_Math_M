from function_storage import *

scale = input("input the scale for M(? X ?):")
scale = int(scale)
A = [[-1] * 5 for i in range (scale)]
B = [[-1] * 5 for i in range (scale)]
C = [[-1] * 5 for i in range (scale)]

print("now input the value for A")
def_array(A,"A",scale)
print("now input the value for B")
def_array(B,"B",scale)
calculate(A,B,C,scale)
convert_to_one(C,scale)
print_array(C)
