from function_storage import *

scale = input("input the scale for M(? X ?):")
scale = int(scale)
A = [[-1] * scale for i in range (scale)]
B = [[-1] * scale for i in range (scale)]
C = [[-1] * scale for i in range (scale)]

print("now input the value for A")
def_array(A,"A",scale)
print("now input the value for B")
def_array(B,"B",scale)
calculate(A,B,C,scale)
print("Before convert, C is :")
print_array(C)
convert_to_one(C,scale)
print("So your A is :")
print_array(A)
print("So your B is :")
print_array(B)
print("your C is: ")
print_array(C)
