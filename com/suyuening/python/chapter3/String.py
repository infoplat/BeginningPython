# coding=utf-8
'''
Created on 2015年11月2日

@author: 岳宁
'''

format1 = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print format1 % values

format2 = "Pi with three decimals:%.3f"
from math import pi
print format2 % pi
print pi

from string import Template
s = Template('$x, glorious $x!')
print s.substitute(x='slum')

s = Template("It's ${x}tastic!")
print s.substitute(x='slum')

s = Template("Make $$ selling $x!")
print s.substitute(x='slum')

s = Template('A $thing must never $action.')
d={}
d['thing']='gentleman'
d['action']='show his socks'
print s.substitute(d)

print '%-10.2f' % pi

print 'With a moo-moo here, and a moo-moo there'.find('moo')

dirs='','usr','bin','env'
print dirs
print '/'.join(dirs)
print 'This is a test'.replace('is', 'eez')

from string import maketrans
table=maketrans('cs', 'kz')
print table

print len(table)
print 'This is an incredible test'.translate(table)
print 'This is an incredible test'.translate(table, " ")