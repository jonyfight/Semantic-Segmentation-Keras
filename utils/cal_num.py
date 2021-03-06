"""
describe:
@project: 智能广告项目
@author: Jony
@create_time: 2019-07-09 12:21:10
@file: dd.py
"""

import json
import os
import csv
import pandas as pd


# 读取json文件，存放到output_json列表里面
def read_json(data_path, hidename):
    output_json = []
    for dirpath, dirnames, filenames in os.walk(data_path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ("." + hidename):
                output_json.append(filename)
    return output_json


# 在单个json文件进行测试
def single_labels(filename):
    labels = []
    with open(os.path.join(path, filename),'r') as load_f:
        file = json.load(load_f)
        shapes = file["shapes"]
        for shape in shapes:
            label = shape["label"]
            labels.append(label)
    return labels


# 得到打标所有名称，保存为list
def t_labels(filepath):
    files = read_json(filepath, "json")
    total_labels = []
    result = []
    for file in files:
        labels = single_labels(file)
        total_labels.append(labels)
    for i in total_labels:
        for j in i:
            result.append(j)
    # lenth = len(total_labels)
    return result


# 去掉list中重复字符串
def main(filepath):
    total = t_labels(filepath)
    seen = set()
    result = []
    for item in total:
        if item not in seen:
            seen.add(item)   # add() 方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。
            result.append(item)
    lenth = len(result)
    save = pd.DataFrame({"result":result})
    save.to_csv("./result.csv", index=False)
    return result, lenth


if __name__=="__main__":
    path = r"F:\BRD_data\Segmentation_BRD\origin\json2"
    print(main(path))
