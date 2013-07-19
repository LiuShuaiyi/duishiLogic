duishiLogic
===========

The logic part of "duishi15"

###逻辑组成员###
朴镜潭(组长)， [刘帅祎](https://github.com/LiuShuaiyi)

----


**一、模块介绍**
-----------
- **shortest**
  
	该模块用于计算单位可以到达的区域。包含函数：
	
	````python
	available_spots(map_list, unit_list, source_num, prev = None)
    ````

  其中，map_list是地图类的二维列表，储存了地图的信息；
  unit_list是一个2 * n的列表，元素为双方各n个单位的对象；
  source_num是要求源单位在unit_list中的index, 即source_num是二元组(side_num,
  object_num), side_num = 0, 1; object_num = 0...n-1;
  prev是用于记录路径的形参。首先，若prev为默认的None，则该功能不被启用。若传入
  列表**不为空**或传入**不是列表**的类型，则函数将不能执行正常功能；当且仅当传
  入**空列表时**函数计算后，传入的list实参prev将变为记录了每个可达点在最短路下
  的前一个点，即prev[i] = j代表返回的available_spots中的第i个点在一条最短路中的
  前一个点是available_spots中的第j个点。通过正权图最短路的性质，可知如此迭代的
  话可由prev和返回值求到任意可到点的一条最短路径。
	


