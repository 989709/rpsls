#coding:gbk
"""
����Ŀ�꣺����for���Ƕ�ף�ʵ������žų˷���
���ߣ��ľ�
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
