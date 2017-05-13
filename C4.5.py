#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import sys
sys.path.append("/path/to/sklearn")
import sklearn

# 加载数据
def loadDataSet(dataPath):  
    dataset = []  
    with open(dataPath) as file:  
        lines = file.readlines()  
        for line in lines:  
            values = line.strip().split(' ')  
            dataset.append(values)  
    return dataset  

# 根据属性值，分割数据集
def splitDataSet(dataset, axis, value):  
    retDataSet = []  
    for featVec in dataset:  
        if featVec[axis] == value:  
            reducedFeatVec = featVec[:axis]  
            reducedFeatVec.extend(featVec[axis+1:])  
            retDataSet.append(reducedFeatVec)  
    return retDataSet  

# 计算数据集的信息熵
def calShannonEnt(dataset):  
    numEntries = len(dataset) * 1.0  
    labelCounts = dict()  
    for featVec in dataset:  
        currentLabel = featVec[-1]  
        if currentLabel not in labelCounts.keys():  
            labelCounts[currentLabel] = 0  
        labelCounts[currentLabel] += 1  
    shannonEnt = 0.0  
    for key in labelCounts:  
        prob = labelCounts[key] / numEntries  
        import math  
        shannonEnt -= prob * math.log(prob, 2)  
    return shannonEnt  

# 计算分割后的数据集相较于原数据集的信息增益
def InfoGain(dataset, axis, baseShannonEnt):  
    featList = [example[axis] for example in dataset]  
    uniqueVals = set(featList)  
    newShannonEnt = 0.0  
    numEntries = len(dataset) * 1.0  
    for value in uniqueVals:  
        subDataSet = splitDataSet(dataset, axis, value)  
        ent = calShannonEnt(subDataSet)  
        prob = len(subDataSet) / numEntries  
        newShannonEnt += prob * ent  
    infoGain = baseShannonEnt - newShannonEnt  
    return infoGain  

# 计算属性的分裂信息值
def SplitInfo(dataset, axis):  
    numEntries = len(dataset) * 1.0  
    labelsCount = dict()  
    ent = 0.0  
    for featVec in dataset:  
        value = featVec[axis]  
        if value not in labelsCount:  
            labelsCount[value] = 0  
        labelsCount[value] += 1  
    for key in labelsCount:  
        prob = labelsCount[key] / numEntries  
        import math  
        ent -= prob * math.log(prob, 2)  
    return ent  

# 计算属性的信息增益率
def GainRate(dataset, baseset, axis, baseShannonEnt):  
    infoGain = InfoGain(dataset, axis, baseShannonEnt)  
    splitInfo = SplitInfo(baseset, axis)  
    return infoGain / splitInfo

# 根据信息增益率，来选择属性
def ChooseBestFeatureByGainRate(dataset, baseset):  
    numFeature = len(dataset[0]) - 1  
    baseShannonEnt = calShannonEnt(dataset)  
    bestGainRate = 0.0  
    bestFeature = -1  
    for i in range(numFeature):  
        gainRate = GainRate(dataset, baseset, i, baseShannonEnt)  
        if gainRate > bestGainRate:  
            bestGainRate = gainRate  
            bestFeature = i  
    return bestFeature

# 构建决策树
def createTree(dataset, baseset, labels):  
    classList = [example[-1] for example in dataset]  
    if classList.count(classList[0]) == len(classList):  
        return classList[0]  
    if len(dataset[0]) == 1:  
        return majorityCnt(classList)  
    bestFeature = ChooseBestFeatureByGainRate(dataset, baseset)  
    bestFeatureLabel = labels[bestFeature]  
    myTree = {bestFeatureLabel:{}}  
    del(labels[bestFeature])  
    featValues = [example[bestFeature] for example in dataset]  
    uniqueVals = set(featValues)  
    for value in uniqueVals:  
        subLabels = labels[:]  
        myTree[bestFeatureLabel][value] = \
         createTree(splitDataSet(dataset, bestFeature, value), baseset, subLabels)  
    return myTree

from sklearn.datasets import load_iris    
from sklearn import neighbors    
import sklearn    
    
#查看iris数据集    
iris = load_iris()    
print iris  


createTree(iris)