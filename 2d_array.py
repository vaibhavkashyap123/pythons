from array import *
new_arr=array('i',[1,2,3,4])
new_arr.append(5)
new_arr.append(6)
print(new_arr)
for i in range(0,len(new_arr)):
    print(new_arr[i])
#revseral of the array
arr=array('d',[1.55,2.555,3.5555,4.55555,5.555555])
arr.reverse()
print(arr)
s=arr.itemsize
print(s)
#--------------------2d array(or multidimenosal array)-----------------------#
import numpy
arr=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
arry=numpy.array([[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
print(arry)
arry.reshape((3,4))
print(arry)
new=numpy.insert(arry,0,[[1,2,3]],axis=0)
print(new)
col_add= numpy.insert(new,1,[1,4,6,5,5],axis=1)
print(col_add)
#append function to add column or row
##axis=1(col add) axis=0(row add)
arr=numpy.array([[0,1],[1,2],[3,4]])
print(arr)
#access the element in the 2d array
def access_element(array,col,row):
    if(len(array)<col or len(array)<row):
        print('index error')
    else:
        print(array[row][col])
arr=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
access_element(arr,2,2)
