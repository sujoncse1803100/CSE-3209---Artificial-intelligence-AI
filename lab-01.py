import pandas as pd
import numpy as np
eps = np.finfo(float).eps
from numpy import log2 as log

path = 'E:/Academic/3-2/CSE 3209 (Artificial Intelligence)/lab/data.csv'
myData = pd.read_csv(path)

# print(myData)
entropy_of_class =0
values=myData.Buy_Computer.unique()
for value in values:
    probublity = myData.Buy_Computer.value_counts()[value]/len(myData.Buy_Computer)
    entropy_of_class = entropy_of_class - probublity*np.log2(probublity)
    
# print(entropy_of_class)

#Age entropy calculation
current_attribute = 'Age'
targets = myData.Buy_Computer.unique()
values = myData[attribute].unique()
entropy_of_age = 0
for val in values:
    entropy_each_feature = 0
    for target in targets:
        num = len(myData[current_attribute][myData[current_attribute]==val][myData.Buy_Computer ==target]) #numerator
        den = len(myData[current_attribute][myData[current_attribute]==val])  #denominator
        p1 = num/(den+eps)
        entropy_each_feature += -p1*log(p1+eps)
    p2 = den/len(myData)
    entropy_of_age += -p2*entropy_each_feature

IG_Age=entropy_of_class-abs(entropy_attribute)
print('Entropy of age attribute = ',abs(entropy_attribute))
print('Information gain of age attribute = ',IG_Age)