
#自定义一个函数my_abs，并规定其参数只能是int型和float型，在参数类型错误时可以抛错
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99)) #输出99
print(my_abs("aaaa")) #抛错，bad operand type

