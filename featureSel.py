import pandas as pd
import itertools
#import numpy as np

combs = [] # includes all subsets
def list_of_combs(arr):
    """returns a list of all subsets of a list"""
    for i in range(2, len(arr)+1):
        listing = [list(x) for x in itertools.combinations(arr, i)]
        combs.extend(listing)
    return combs
# x , file that has .csv extension
#s, user given inconsistency rate that is less than  
#data = pd.read_csv('feature.csv')  
    
data2 = pd.read_csv('FIFA_2018_StatisticsV2.csv')  
df2=data2.iloc[:,3:] # remove first three column

cleanup_nums = {"WLD":     {"D": 0, "L": 1 ,"W":2},
                "Man_of_the_Match": {"No": 0, "Yes": 1},
                "Round":    {"3rd Place": 1, "Final": 2, "Group Stage":3, "Quarter Finals": 4,
                             "Round of 16": 5, "Semi- Finals": 6},
                "PSO":  {"No":1 ,"Yes":0 } }
                
df2.replace(cleanup_nums, inplace=True)
df2 = df2.fillna(0)

def filter(row):
    if row['Passes'] <= 281:
        return 1
    elif row['Passes'] <= 338:
        return 2 
    elif row['Passes'] <= 379:
        return 3 
    elif row['Passes'] <= 424:
        return 4 
    elif row['Passes'] <= 473:
        return 5 
    elif row['Passes'] <= 520:
        return 6 
    elif row['Passes'] <= 547:
        return 7 
    elif row['Passes'] <= 594:
        return 8 
    elif row['Passes'] <= 669:
        return 9 
    elif row['Passes'] <= 732:
        return 10 
    elif row['Passes'] <= 805:
        return 11 
    else:
        return 12

df2['Passes'] = df2.apply(filter, axis=1)
                
def func(data,s):
    #data = pd.read_csv(x) # get dataframe object
    columnIndex=data.shape[1] # column number of df object, feature number + class label
    
    feature_index=list(range(columnIndex-1)) #remove class label by -1
    # man of match datası için 18.column çıkmalı
    list_of_combs(feature_index) # get all combinations of feature set
    min_inconsistency_rate=s
    selected_features_comb =0 
    for x in range(len(combs)):
        subset = combs[x] # feature indexes
        df = data.iloc[:,subset] # data frame 
        #subset_size=df.size
        inconsistency_set_number =0
        subset_size=df.shape[0] # row number
        class_labels=list(data.groupby(list(df))[list(data)[18]].nunique()) # take category number each same row value
        label_num=list(data.groupby(list(df))[list(data)[18]].value_counts()) # which one and how many?
        z=0    
        for y in range(len(class_labels)):
            if class_labels[y]>1:
                set=label_num[z:class_labels[y]+z]
                inconsistency_num=sum(set)-max(set) # take different class labels 
                inconsistency_set_number +=inconsistency_num
                z=z+class_labels[y]
            else:
                z=z+1
        inconsistency_rate=inconsistency_set_number/subset_size
        #print(inconsistency_rate) #  inconsistency_rate of  subsets
        if inconsistency_rate< min_inconsistency_rate:
            min_inconsistency_rate= inconsistency_rate
            selected_features_comb=x
    df = data.iloc[:,combs[selected_features_comb]]
    print(min_inconsistency_rate) # inconsistency rate
    return  list(df)     # list of selected fetures with column names   

def selected(data,subset):
    df = data.iloc[:,subset] # data frame
    subset_size=df.shape[0] # row number,pattern number
    class_labels=list(data.groupby(list(df))[list(data)[18]].nunique()) # take category number each same row value
    label_num=list(data.groupby(list(df))[list(data)[18]].value_counts()) # which one and how many?
    inconsistency_set_number =0
    z=0    # z index value for label_num list 
    for y in range(len(class_labels)):
         if class_labels[y]>1:
                set=label_num[z:class_labels[y]+z]
                inconsistency_num=sum(set)-max(set) # take different class labels 
                inconsistency_set_number +=inconsistency_num
                z=z+class_labels[y]
         else:
             z=z+1
    
    inconsistency_rate=inconsistency_set_number/subset_size
    print(inconsistency_rate)
    return data.groupby(list(df))[list(data)[18]].value_counts() # which one and how many?


subset=[0,1,5,20,21,22,23,24]
selected(df2,subset)              
func(df2,10)            
        

