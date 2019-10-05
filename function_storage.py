def def_row(x):
    pass

def print_array(array):
    for i,j in enumerate(array):
        print (j)
    print ("\n....................")


def def_array(array,name,scale):
    for i in range(scale):
        for j in range(scale):
            value = input("please input value for [" + str(i)+"]" + "[" + str(j) + "] (input integer only)")
            value = int(value)
            array[i][j] = value
            print ("now " + name + " is")
            print_array(array)


def convert_to_one(array,scale):
    for i in range(scale):
        for j in range(scale):
            if array[i][j] >= 1:
                array[i][j] = 1



def calculate(array_A,array_B,array_C,scale):
    sum = 0
    x = 0
    y = 0
    for z in range(scale):
        for j in range(scale):
            sum = 0
            for i in range(scale):
                if i == scale - 1:
                    temp = array_A[x][i] * array_B[i][y]
                    sum = sum + temp
                    array_C[x][y] = sum
                    y = y + 1
                    if y == scale :
                        x = x + 1
                        y = 0
                else:
                    temp = array_A[x][i] * array_B[i][y]
                    sum = sum + temp

def print_detail(array_A,array_B,array_C,scale):
    x = 0
    y = 0
    for z in range(scale):
        for j in range(scale):
            sum_str = ""
            sum_num = 0
            for i in range(scale):
                if i == scale - 1:
                    temp_str = str("(%d)(%d) + " % (array_A[x][i],array_B[i][y]))
                    sum_str = sum_str + temp_str
                    temp_num = array_A[x][i] * array_B[i][y]
                    sum_num = sum_num + temp_num
                    array_C[x][y] = sum_num
                    y = y + 1
                    print ("c[%d][%d] : %s = %d \n" % (x+1,y,sum_str,sum_num))
                    if y == scale :
                        x = x + 1
                        y = 0
                else:
                    temp_str = str("(%d)(%d) +" % (array_A[x][i],array_B[i][y]))
                    temp_num = array_A[x][i] * array_B[i][y]
                    sum_num = sum_num + temp_num
                    sum_str = sum_str + temp_str

def ask_if_detail(A,B,C,scale):
    ask = input("Do you need detail? Input 1 for yes, 0 for no :")
    ask = int(ask)
    if ask == 1:
        print_detail(A,B,C,scale)
    else:
        print("End")

def print_result(A,B,C,scale):
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
