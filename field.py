# -*- coding: cp936 -*-
import basic

def construct_map(kind):
    "�������͹����ͼ����(�����ص�������)"
    if kind == basic.TURRET:
        return basic.Map_Turret(kind)
    elif kind == basic.TEMPLE:
        return basic.Map_Temple(kind)
    else:
        return basic.Map_Basic(kind)

def get_position(string):
    x=(ord(string[0])-48)*10+(ord(string[1])-48)
    y=(ord(string[3])-48)*10+(ord(string[4])-48)
    return (x,y)

map_file=open("Map.txt","r")
whole_map=[];Gear=[];base=[[],[]]
map_temple=[]#��¼��ÿ�غϼ���������λ��
s=0;i=0
while 1:
    string=map_file.readline()
    if string=="\n":
        break
    m=[];j=0
    for c in string[:-1]:
        kind=ord(c)-48
        m+=[construct_map(kind)]
        if kind==TEMPLE:
            map_temple+=(i,j)
        if kind==GEAR:
            s+=1
        j+=1
    whole_map+=[m]
    i+=1
for i in range(1,s+1):
    string=map_file.readline()
    gear_position=get_position(string[:5])
    gear_control=[]
    while 1:
        if not string:
            break
        string=string[6:]
        if string=='\n':
            break
        gear_control+=[get_position(string[:5])]
    whole_map[gear_position[0]][gear_position[1]]=Map_Gear(GEAR,gear_control)
#����������ֵ�ͼת��Ϊ���͵�ͼ        
for i in [0,1]:
    string=map_file.readline()
    while string!='\n':
        c=string[0]
        position=get_position(string[2:7])
        if ord(c)-48==WIZARD:
            base[i]+=[Wizard(ord(c)-48,position)]
        else:
            base[i]+=[Base_Unit(ord(c)-48,position)]
        string=string[8:]
#����ʿ��    
#�ļ�����:whole_map��ʾ��������    
#        base[0],base[1]�б��ʾʿ��
