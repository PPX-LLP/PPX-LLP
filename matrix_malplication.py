import numpy as np
# 矩阵输入
first=input("please key in the left matrix,split different rows with ','\n")
a_l,a_w=input("l,w\n").split()
a_l=int(a_l)
a_w=int(a_w)
second=input("please key in the right matrix,split different rows with ','\n ")
b_l,b_w=input("l,w\n").split()
b_l=int(b_l)
b_w=int(b_w)
left=(np.fromstring(first,dtype=int,sep=',')).reshape(a_l,a_w)
right=(np.fromstring(second,dtype=int,sep=',')).reshape(b_l,b_w)
# 矩阵乘积
def matrix_malplication(a,b):
    a_maxdim=a.ndim
    b_maxdim=b.ndim
    if(a.shape[1]==b.shape[0]):
        a_l=a.shape[0]
        a_w=a.shape[1]
        b_l=b.shape[0]
        b_w=b.shape[1]
        c=np.zeros((a_l,b_w))
        for i in range(0,a_l):
            for j in range(0,b_w):
                for k in range(0,a_w):
                    c[i,j]+=a[i,k]*b[k,j]
        return c
    else:
        print("incorrect result")
        return None
# 结果检验
# a=(matrix_malplication(left,right))
# b=(np.dot(left,right))
if np.array_equal(a,b):
    print("Correct")
else:
    print("False")