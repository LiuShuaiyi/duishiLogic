# -*- coding: cp936 -*-
'''
	������Ϊshortest��pythonģ�飬�ṩ�����ڽ������ʽ15��
	�߼���������Ҫ�Ŀ��Ե����������ĺ�����ʹ�õ������ص�
	Dijkstra�㷨��
'''
import basic
import field

def available_spots(map_list, unit_list, source_num):
    '''�ú������ڼ��㵱ǰ��ͼ��ĳ��λ�Ļ��Χ��
   �������map_list��Ϊ������ͼ��Ԫ�Ķ�ά����
   �����˵�ͼ��ȫ����Ϣ��unit_listͬ����¼������
   ��λ����Ϣ��source_num��һ��Ԫ�飬Ϊ(side_num, object_num)
    '''
    #���㵥λ�赲��λ��
    u_block = [unit_list[i][j].position \
               for i in range(2) for j in range(len(unit_list[i]))]
    d_spots = [] # �����Ѿ�ȷ���ɵ����ɳ���ϵĵ�
    a_spots = [] # ���б��ɳڹ���δȷ���ɵ��ĵ�
    a_weight = [] # ���е�Ȩֵ
    " ��Դ�����(��ע������Ĭ�ϵ�ͼ����һȦ)"
    s_unit = unit_list[source_num[0]][source_num[1]] # Ŀ�굥λ
    s_position = s_unit.position # Դ������
    a_spots = [s_position]
    a_weight = [0]
    while len(a_spots) != len(map_list) * len(map_list[0]):
        min_weight = min(a_weight) # ��a_weight����Сֵ
        if min_weight >= s_unit.move_range: # ���Ｋ��
            break
        s = a_weight.index(min_weight) # ȡ�������
        # �ɳڲ���
        p_modify = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for i in range(4):
            p = a_spots[s] + p_modify # �����ɳڵ��ĸ������
            if not (p in u_block or p in d_spots): # �ɳڵ������
                if p in a_spots: # ����
                    lf = map_list[p[0]][p[1]].landform
                    p_id = a_spots.index(p)
                    if MOVE_COST[lf] + a_weight[s] < a_weight[p_id]:
                        a_weight[p_id] = MOVE_COST[lf] + a_weight[s]
                    else: 			#�¼���
                        lf = map_list[p[0]][p[1]].landform
                        a_spots.append(p)
                        a_weight.append(a_weight[s] + MOVE_COST[lf])
        # �ɳڽ����󣬽� s ��a����ɾ���� �������뵽d������
        d.append(a_spots[s])
        a_spots.pop(s)
        a_weight.pop(s)

    return d_spots

def main():
    pass

if __name__ == '__main__':
    main()


