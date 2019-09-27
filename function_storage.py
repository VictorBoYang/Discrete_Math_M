def def_row(x):
    pass

def print_array(array):
    for i,j in enumerate(array):
        print (j)
    print ("\n....................")

def def_array(array,name,scale):
    for i in range(scale):
        for j in range(scale):
            value = input("please input value for [" + str(i)+"]" + "[" + str(j) + "]")
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
