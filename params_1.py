
#定义一个函数power，n为默认参数，默认=2，所以power(5)的意思就是5^2、power(5,4)的意思是5^4
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))  #25
print(power(5, 4))  #625