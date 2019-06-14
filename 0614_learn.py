#内部字符编码声明
# -*- coding: utf-8 -*-

#多赋值
x,y = 2,3
print('x =',x,'y =',y) #字符串,分割拼接 => x = 2 y = 3 (,会变成空格)
#int   整数
#float 总是包括一个小数点
#bool  true,flase
#None  空?
print(6 // 4) #只取整 => 1
print(type(6 / 4)) #class float => 1.5
print(2 ** 3) #阶乘 2的三次方 => 8
print(2 * 3) #2 乘以 3  => 6

#===================分割线=====================
# if Boolean expression:  if判断 + 条件:
#elif Boolean expression:  -> 相当于其他语言的 elseif
if 5 / 2 != 0:
    print('true')
else: #严格缩进。
    print('false')
print('这里就不属于else了')

if 5 / 2 != 0:
    if 5 / 2 == 0:
        print('true true')
    else:
        print('true','false')
elif 1 != 2:
    print('1 != 2')

#==================分割线===========================


str = 'this is str'
print(len(str)) #len 字符串长度 一个空格也占一个位置 => 11
print(str[2]) #[] 取出下标对应的字符串 下标为0
print(str[5:len(str)]) #从下标5开始取出 直到最后

#   n = input('please input age:') #input 让用户输入自己需要获取到的值
#   print(type(n)) #获取到的是 str类型的值






