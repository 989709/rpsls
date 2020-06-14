#coding:gbk
"""
程序目标：实现在屏幕上输出”百钱买百鸡“问题的所有可能解决方案
作者:夏晶
"""

print("百钱买百鸡的解决方案为：")
for big in range(0,20):
	for big1 in range(0,33):
		for small in range(0,300):
			sum=big+big1+small
			sum_money=(big*5)+(big1*3)+(small/3)
			if sum==100 and sum_money==100:
				print("母鸡%d只，公鸡%d只，小鸡%d只"%(big1,big,small))

