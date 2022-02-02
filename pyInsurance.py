import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#empty lists to organize data
age =[]
sex =[]
bmi =[]
children =[]
smoker =[]
region =[]
charges =[]
#load data
insurance = open('insurance.csv','r')
file = csv.DictReader(insurance)
#appending to lists
for col in file:
    age.append(int(col['age']))
    sex.append((col['sex']))
    bmi.append(float(col['bmi']))
    children.append(int(col['children']))
    smoker.append(col['smoker'])
    region.append(col['region'])
    charges.append(float(col['charges']))                               
#create dictionary for
#bmi sex
dict1 = {key:[bmi[idx]
       for idx in range(len(bmi)) if sex[idx]==key]
       for key in set(sex)}
#age sex
age_sex = {key:[age[idx]
       for idx in range(len(age)) if sex[idx]==key]
       for key in set(sex)}
#Function for finding average
def average(dict):
    for key in dict:
        avg_list = [sum(dict[key]) / len(dict[key])]
        dict[key] = avg_list
    print(dict)
#Results
average(age_sex)
average(dict1)
#Pandas-Information about the data set
df = pd.read_csv("insurance.csv")
print(df.head())
print(df.info())
#Pandas-Selecting columns for analisis
pd_age_sex = df.groupby('sex').age.mean()
pd_bmi_age = df.groupby('age').bmi.mean()
#print(type(pd_age_sex)) is dataframe
pd_age_sex.plot(x ='sex', y = 'age', kind = 'bar')
pd_bmi_age.plot(x = 'age', y = 'bmi', kind = 'bar')
plt.show()