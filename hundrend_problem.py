#coding:gbk
"""
����Ŀ�꣺ʵ������Ļ���������Ǯ��ټ�����������п��ܽ������
����:�ľ�
"""

print("��Ǯ��ټ��Ľ������Ϊ��")
for big in range(0,20):
	for big1 in range(0,33):
		for small in range(0,300):
			sum=big+big1+small
			sum_money=(big*5)+(big1*3)+(small/3)
			if sum==100 and sum_money==100:
				print("ĸ��%dֻ������%dֻ��С��%dֻ"%(big1,big,small))

