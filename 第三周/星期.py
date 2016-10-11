#week.py
#coding=utf-8
'''
将所有周数存储在字符串中
在字符串中截取适当的字串来查找特定周数
每个周几由4个字符组成，如果pos表示第一个字母那么weeks[pos:pos+3]表示这个周数的缩写
'''
weeks="Mon.TuesWed.ThurFri."
n = input("请输入周几（1-7）：")
pos=(int(n)-1) * 4
weekDay=weeks[pos:pos+4]
print("本周是"+weekDay+".")