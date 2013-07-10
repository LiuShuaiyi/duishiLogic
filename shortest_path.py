'''
	这是名为shortest_path的python模块，提供了用于解决“队式15”
	逻辑部分所需要的可以到达区域计算的函数。使用的是朴素的
	Dijkstra算法。
'''

def available_spots(map_list, unit_list, source_num):
'''该函数用于计算当前地图下某单位的活动范围。
   传入参量map_list，为基本地图单元的二维数组
   储存了地图的全部信息。unit_list同样记录了所有
   单位的信息。source_num是一个元组，为(side_num, object_num)
'''
	#计算单位阻挡的位置
	u_block = [unit_list[i][j].position for i in range(2) for j in range(len(unit_list[i]))]

	d_spots = [] # 所有已经确定可到且松弛完毕的点
	a_spots = [] # 所有被松弛过，未确定可到的点
	a_weight = [] # a_spots的点中的权值

	# 将源点加入(备注：这里默认地图加了一圈)
	s_unit = unit_list[source_num[0]][source_num[1]] # 目标单位
	s_position = s_unit.position # 源点坐标
	a_spots = [s_position]
	a_weight = [0]
	while len(a_spots) != len(map_list) * len(map_list[0]):
		min_weight = min(a_weight) # 求a_weight中最小值
		if min_weight >= s_unit.move_range: # 到达极限
			break
		s = a_weight.index(min_weight) # 取得其序号
		# 松弛操作
		p_modify = ((1, 0), (-1, 0), (0, 1), (0, -1))
		for i in range(4):
			p = a_spots[s] + p_modify # 可以松弛的四个方向点
			if not (p in u_block or p in d_spots): # 松弛点的条件
				if p in a_spots: # 更新
					lf = map_list[p[0]][p[1]].landform
					p_id = a_spots.index(p)
					if MOVE_COST[lf] + a_weight[s] < a_weight[p_id]:
						a_weight[p_id] = MOVE_COST[lf] + a_weight[s]
				else: 			#新加入
					lf = map_list[p[0]][p[1]].landform
					a_spots.append(p)
					a_weight.append(a_weight[s] + MOVE_COST[lf])

		# 松弛结束后，将 s 从a序列删除， 将它加入到d序列中
		d.append(a_spots[s])
		a_spots.pop(s)
		a_weight.pop(s)
	return d_spots

	