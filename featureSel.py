import pandas as pd
import itertools

combs = [] # includes all subsets
def list_of_combs(arr):
    """returns a list of all subsets of a list"""
    for i in range(2, len(arr)+1):
        listing = [list(x) for x in itertools.combinations(arr, i)]
        combs.extend(listing)
    return combs
# x , file that has .csv extension
#s, user given inconsistency rate that is less than  
data = pd.read_csv('feature.csv')    
def func(data,s):
    #data = pd.read_csv(x) # get dataframe object
    columnIndex=data.shape[1] # column number of df object, feature number + class label
    
    feature_index=list(range(columnIndex-1)) #remove class label by -1
    list_of_combs(feature_index) # get all combinations of feature set
    min_inconsistency_rate=s
    selected_features_comb =0 
    for x in range(len(combs)):
        subset = combs[x] # feature indexes
        df = data.iloc[:,subset] # data frame 
        subset_size=df.size
        inconsistency_set_number =0
        #subset_size=df.shape[0] # row number
        class_labels=list(data.groupby(list(df))[list(data)[-1]].nunique()) # take category number each same row value
        label_num=list(data.groupby(list(df))[list(data)[-1]].value_counts()) # which one and how many?
        for y in range(len(class_labels)):
            if class_labels[y]>1:
                set=label_num[y:label_num[y]+y]
                inconsistency_num=sum(set)-max(set) # take different class labels 
                inconsistency_set_number +=inconsistency_num
         
        inconsistency_rate=inconsistency_set_number/subset_size
        if inconsistency_rate< min_inconsistency_rate:
            min_inconsistency_rate= inconsistency_rate
            selected_features_comb=x
    df = data.iloc[:,combs[selected_features_comb]]
    print(min_inconsistency_rate) # inconsistency rate
    return  list(df)     # list of selected fetures with column names   

                
func(data,10)            
        

