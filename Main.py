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

print_result(A,B,C,scale)
ask_if_detail(A,B,C,scale)
