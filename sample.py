# -*- coding: utf-8 -*-

"""
    usage for shogun-toolbox

    explained in detail http://qiita.com/ysak/items/20cd4e7db9a7c3f79f10
"""


"""
    generate and set/get values to Labels
"""
def label_function():
    from modshogun import BinaryLabels
    from modshogun import CSVFile

    #generate random labels 
    label = BinaryLabels(5)

    print label.get_num_labels()
    #→ 5

    print label.get_values()
    #→ array([5 label values])

    #Labels from CSVFile
    label_from_csv = BinaryLabels(CSVFile("csv/label.csv"))


"""
    generate and set/get values to Features
"""

def feature_function():
    
    from modshogun import RealFeatures
    from modshogun import CSVFile
    import numpy as np

    #3x3 random matrix 
    feat_arr = np.random.rand(3, 3)
    
    #initialize RealFeatures from numpy array
    features = RealFeatures(feat_arr)

    #get matrix value function
    print features.get_feature_matrix(features)
    
    #get selected column of matrix
    print features.get_feature_vector(1)

    #get number of columns
    print features.get_num_features()

    #get number of rows
    print features.get_num_vectors()
    
    feats_from_csv = RealFeatures(CSVFile("csv/feature.csv"))
    print "csv is ", feats_from_csv.get_feature_matrix()



if __name__ == "__main__":
    
    feature_function()

