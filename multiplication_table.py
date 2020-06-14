#coding:gbk
"""
程序目标：利用for语句嵌套，实现输出九九乘法表
作者：夏晶
"""
def name(sum):
	for i in range(1,10):
		for j in range(1,10):
			sum=i*j
			if i>=j:
				print("%sx%s=%s"%(i,j,sum),end=" ")
		print()
	return name
name(sum)
