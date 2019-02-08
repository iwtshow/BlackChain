from  itertools import *
#count的用法 count(start,step)
# for i in zip(count(1,2),["a","b","c"]):
#     print(i)

#repeat 的用法repeat(object,times)  如果times=None  则无限打印object
# for i in repeat("hello_world",5):
#     print(i)

#chain  将多个迭代器作为参数，但只返回单个迭代器
# a = [1,2,3,4,5]
# b = ["l","i","u","f","y"]
# c = ["N","n"]
# for i in chain(a,b,c):
#     print(i)

#dropwhile  只要should(x)为True,则继续执行should(x)函数，否则，后续所有项不再调用should
#
# def  should(x):
#     print("test : %d"%x)
#     return (x>0)
#
# for i in dropwhile(should,[-1,-2,1,0,2,3,-4]):
#     print("start : %d"%i)




