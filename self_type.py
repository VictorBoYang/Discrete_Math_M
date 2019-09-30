from function_storage import *
#This is also one test, This is the example from Chris, you can change number and type by yourself

scale = 5  #can change scale
A = [
[1,0,0,0,0],
[0,0,1,0,0],
[0,0,0,0,0],
[1,1,0,0,0],
[0,0,0,0,0]]
B = [
[1,0,0,1,0],
[0,0,0,1,0],
[0,1,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]]
#can change number for A/B

C = [[-1] * 5 for i in range(scale)]

print_result(A,B,C,scale)
