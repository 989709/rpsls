#coding:gbk
"""
����Ŀ�꣺ͨ���Զ��庯����ʵ��RPSLS��Ϸ��{�û�ͨ��������������һ��ѡ��ʯͷ/����/��/
         ����/ʷ���ˣ���������Զ�����һ�����ѡ�񣬸���RPSLS���򣬲������յĽ��}
���ߣ��ľ�
"""

import random



# 0 -rock ʯͷ
# 1 -Spock ʷ����
# 2 - paper��
# 3 - lizard����
# 4 - scissors����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=='ʯͷ':
        print("����ѡ��Ϊ:%s"%(name))
        name=0
    elif name=='ʷ����':
        print("����ѡ��Ϊ:%s"%(name))
        name=1
    elif name=='��':
        print("����ѡ��Ϊ:%s"%(name))
        name=2
    elif name=='����':
        print("����ѡ��Ϊ:%s"%(name))
        name=3
    elif name=='����':
        print("����ѡ��Ϊ:%s"%(name))
        name=4
    else:
        print("Error: No Correct Name")
    return name


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        computer_print='ʯͷ'
        print("�������ѡ��Ϊ��ʯͷ")
        number=0
    elif number==1:
        computer_print='ʷ����'
        print("�������ѡ��Ϊ��ʷ����")
        number=1
    elif number==2:
        computer_print='��'
        print("�������ѡ��Ϊ����")
        number=2
    elif number==3:
        computer_print='����'
        print("�������ѡ��Ϊ������")
        number=3
    else:
        computer_print='����'
        print("�������ѡ��Ϊ������")
        number=4
    return number

    


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print("---------------------")
    if choice_name=='ʯͷ' or choice_name=='����' or choice_name=='ʷ����' or choice_name=='����' or choice_name=='��':
        player_choice_number=name_to_number(choice_name)
        comp_number=random.randrange(0,5)
        number_to_name(comp_number)
        if player_choice_number==0 and comp_number==3 :
            print("��Ӯ��")
        elif player_choice_number==0 and comp_number==4:
            print("��Ӯ��")
        elif player_choice_number==1 and comp_number==4:
            print("��Ӯ��")
        elif player_choice_number==1 and comp_number==0:
            print("��Ӯ��")
        elif player_choice_number==2 and comp_number==0:
            print("��Ӯ��")
        elif player_choice_number==2 and comp_number==1:
            print("��Ӯ��")
        elif player_choice_number==3 and comp_number==2:
            print("��Ӯ��")
        elif player_choice_number==3 and comp_number==1:
            print("��Ӯ��")
        elif player_choice_number==4 and comp_number==3:
            print("��Ӯ��")
        elif player_choice_number==4 and comp_number==2:
            print("��Ӯ��")
        elif player_choice_number==comp_number:
            print("���ͻ�����ѡ��һ�������Դ˾�ƽ��")
        else:
            print("����Ӯ��")
    else:
	    name_to_number(choice_name)
   
    


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
