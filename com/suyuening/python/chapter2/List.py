# coding=utf-8
'''
Created on 2015年11月1日

@author: 岳宁
'''

su = ['Su Yuening', 33]
shan = ['Zhang Shanshan', 32]
database = [su, shan]
print database

# 索引
greeting = 'Hello'
print greeting[0]

numbers = [1, 2, 3, 4, 5] + [6, 7, 8, 9, 10]

print numbers
print numbers[3:6]
print numbers[-3:-1]
print numbers[-3:]
print numbers[:3]
print numbers[:]
print numbers[0:10:2]
print numbers * 5
print 5 * '*'

permissions = "rw"
print 'r' in permissions
print 'a' in permissions

for one in permissions:
    print one
# users = ['mlh', 'foo', 'bar']
# print raw_input('Enter your user name:') in users
subject = '$$$ Get rich now!!! $$$'
print '$$$' in subject

print len(numbers)
print max(numbers)
print min(numbers)

print list(permissions)
print ','.join(list(permissions))

x = ['1', 1, 1]
print x
x[0] = 2
print x
x[1] = permissions
print x
del x[1]
print x

numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print numbers
numbers.append(6)
print numbers

countlist = ['to', 'be', 'or', 'not', 'to', 'be']
print countlist.count('to')
print countlist.count('or')

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print a
a.insert(3, 'four')
print a
print a.pop()
print a
a.reverse()
print a
x = [4, 6, 2, 1, 7, 9]
# y=x[:]
# y.sort()
# y = sorted(x)
# print x
# print y

z = x[:]

cmp(1, 1)
print z
z.sort(cmp)
print z

abc = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
abc.sort(cmp=cmp,key=len)
print abc
