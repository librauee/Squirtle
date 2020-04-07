# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:37:28 2020

@author: 老肥
@WeChat Official Accounts:老肥码码码
@Wechat: jennnny1216

Happy Python，Happy Life!
"""

from sklearn import svm
import numpy as np
import _pickle as cPickle
import os
import shutil
import math


def get_matrix(file,batch_size):
    """
    获取特征向量和标签
    """
    file_list=os.listdir(file)
    feature_matrix=cPickle.load(open(os.path.join(file,'data_0.pickle'),'rb'))
    origin_labels=list(feature_matrix[-1])
    feature_matrix=np.asarray(feature_matrix[:-1])
    feature_matrix=feature_matrix.reshape(batch_size,2048)
    for i in range(1,len(file_list)):
        temp_feature_matrix=cPickle.load(open(os.path.join(file,'data_{}.pickle'.format(i)),'rb'))
        origin_labels.extend(list(temp_feature_matrix[-1]))
        temp_feature_matrix=np.asarray(temp_feature_matrix[:-1])
        temp_feature_matrix=temp_feature_matrix.reshape(batch_size,2048)
    
        feature_matrix=np.vstack((feature_matrix,temp_feature_matrix))
    return feature_matrix,origin_labels
    

def move(src,dst,i):
    """
    移动同一个聚类的表情包到同一个文件夹中
    """
    if not os.path.isdir(dst):
        os.makedirs(dst)
    s=os.path.join(src,'{}.jpg'.format(i))
    d=os.path.join(dst,'{}.jpg'.format(i))
    shutil.copy(s,d)

def one_class_svm():
    model=svm.OneClassSVM()
    feature_matrix,_=get_matrix('data_jieni',50)
    model.fit(feature_matrix)
    vedieo_feature_matrix,origin_labels=get_matrix('data_vedio',500)
    result=model.predict(vedieo_feature_matrix)
    print(result)
    for i in range(len(origin_labels)):
        if result[i]==1:
            print(origin_labels[i])
            move(src='vedio',dst='result',i=origin_labels[i])


if __name__=='__main__':
    one_class_svm()