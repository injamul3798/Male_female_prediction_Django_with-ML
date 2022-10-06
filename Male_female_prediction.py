#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_csv
from sklearn.metrics import accuracy_score
from pandas import to_pickle,read_pickle
from sklearn.model_selection import train_test_split

df = pd.read_csv(r"C:\\Users\\HP\\Downloads\\archive (3)\\gender_classification_v7.csv")

x = df.iloc[:,:-1]
y = df['gender']

#spliting data set into train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30,random_state=1)

##fit traing dataset into model decition tree
from sklearn.tree import DecisionTreeClassifier  
model= DecisionTreeClassifier(criterion='entropy', random_state=0)  
model.fit(x_train, y_train)  

#predictions
predictions = model.predict(x_test)

#
pd.to_pickle(model,r"C:\Users\HP\Music\new_model1.pickle")
model = pd.read_pickle(r"C:\Users\HP\Music\new_model1.pickle")


long_hair = float(input("Enter long_hair :"))
forehead_width_cm = float(input("Enter forehead width_cm :"))
forehead_height_cm = float(input("Enter forehead height_cm:"))
nose_wide = float(input("Enter nose_wide: "))
nose_long = float(input("Enter nose_long: "))
lips_thin = float(input("Enter lips_thin: "))
distance_nose_to_lip_long = float(input("Enter distance_nose_to_lip_long: "))
result = model.predict([[long_hair,forehead_width_cm,forehead_height_cm,nose_wide,nose_long,lips_thin,distance_nose_to_lip_long]])
print(result)


# In[15]:





# In[ ]:




