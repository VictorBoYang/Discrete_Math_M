from function_storage import *
#This is also one test, This is the example from Chris
A = [[1,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,0]]
B = [[1,0,0,1,0],[0,0,0,1,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
C = [[-1] * 5 for i in range(5)]
calculate(A,B,C,5)

convert_to_one(C,5)

print_array(C)
