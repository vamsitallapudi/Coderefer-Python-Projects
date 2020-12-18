
# def func(*args, **kwargs):
#     for arg in args:
#         print(arg)
#
#     for arg in kwargs:
#         print(arg)

def myfunc(*args, **kwargs):
    for arg in args:
        print(arg)

    for item in kwargs.items():
        print(item)

myfunc(21,x=345,y=20,)
# func(1,2,3,4, "vamsi", l)