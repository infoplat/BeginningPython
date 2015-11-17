# coding=utf-8
class Human(object):
    def __init__(self, input_gender):
        self.gender = input_gender
    def printGender(self):
        print self.gender

li_lei = Human('male') # 这里，'male'作为参数传递给__init__()方法的input_gender变量。
print li_lei.gender   #这一行结果与下一行对比
li_lei.printGender()   #这一行结果与上一行对比