#-*- coding:utf-8 -*-

import random
import copy

#计算两个样本的欧式距离
def compute_distance(s1,s2):
    res = 0
    for a,b in zip(s1,s2):
        res += 1.0*(a-b)*(a-b)
    return res ** 0.5

#计算样本集合的均值向量
def compute_average(slist):
    average_list = [0] * len(slist[0])
    for i in range(len(slist)):
        for j in range(len(slist[i])):
            average_list[j] += slist[i][j]
    for i in range(len(average_list)):
        average_list[i] = 1.0*average_list[i]/len(slist)
    return average_list


#找出当前不再质心集合中样本 与 质心样本的距离最大的样本
def find_centroid(data,N,s):
    centroid = -1
    max_distance = 0
    for i in range(N):
        if i in s:
            continue
        for j in s:
            dis = compute_distance(data[i],data[j])
            if dis > max_distance:
                centroid = i
                max_distance = dis
    return centroid

def clustering(data, k):

    N,m = len(data),len(data[0])
    #1.初始化质心集合，s
    s = []
    #2.随机选取样本点，加入s
    init_sample = int(N*random.random())
    s.append(init_sample)
    #3.找出k个质心
    while len(s) < k:
        centroid = find_centroid(data, N, s)
        s.append(centroid)
    #4.遍历样本点,计算与质心距离并分配
    centroid_dict = {}#质心index及对应的向量
    for i in range(len(s)):
        centroid_dict[i] = data[s[i]]
    sample_centroid_list = []#存储每个样本的质心index
    for i in range(N):
        min_dis = -1
        i_centroid = -1
        for j in range(len(s)):
            dis = compute_distance(data[i],data[s[j]])
            if min_dis == -1 or dis<min_dis:
                i_centroid = j
                min_dis = dis
        sample_centroid_list.append(i_centroid)
    #5.迭代质心,直到每个样本的质心不在变化
    while True:
        tmp_centroid_dict = {}
        tmp_sample_centroid_list = []
        centroid_group_dict = {}
        for sample_centroid_index in sample_centroid_list:
            if sample_centroid_index not in centroid_group_dict:
                centroid_group_dict[sample_centroid_index] = []
            centroid_group_dict[sample_centroid_index].append(centroid_dict[sample_centroid_index])
        for i,v in zip(range(len(centroid_group_dict)),centroid_group_dict.values()):
            tmp_centroid_dict[i] = compute_average(v)
        for i in range(N):
            min_dis = -1
            i_centroid = -1
            for j,v in tmp_centroid_dict.iteritems():
                dis = compute_distance(data[i],v)
                if min_dis == -1 or dis<min_dis:
                    i_centroid = j
                    min_dis = dis
            tmp_sample_centroid_list.append(i_centroid)
        flag = True
        for a,b in zip(sample_centroid_list,tmp_sample_centroid_list):
            if centroid_dict[a] != tmp_centroid_dict[b]:
                flag = False
        if flag:
            return tmp_sample_centroid_list
        else:
            centroid_dict = copy.deepcopy(tmp_centroid_dict)
            sample_centroid_list = copy.deepcopy(tmp_sample_centroid_list)

if __name__ == '__main__':
    data = [
        [1,1],
        [2,2],
        [3,3],
        [100,100],
        [101,101],
        [102,102],
    ]
    print clustering(data,2) 
