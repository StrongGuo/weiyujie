print('hello, world')
print(r'\\\t\\') #r'...'标识r后面的''里面的字符都不用转义
print('\\\t\\')
print('''line1
... line2
... line3''')  #'''...'''可以代替\n换行
print('aaa\nbbb')  #\n用于换行
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)




listA = ['a', 'b', 'c'] # listA是一个数列
list_length = len(listA) #list_length是数列listA的长度
print(list_length)



#python中的for循环，可用于累加数字；range（10）表示生成从0到10的正整数序列
sum = 0
for x in range(10):
    sum = sum + x
print(sum)

#另一个for循环的例子
L = ['Bart', 'Lisa', 'Adam']
for a in L:
    print('Hello, ' + a + '!')


#python中还有while循环，一直循环到不满足while条件退出，可用break提前退出循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')


# continue语句用于跳过循环中的某些条件下的步骤，例如下面的表示跳过1~10中的偶数
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue 
    print(n)




