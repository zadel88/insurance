import csv
import statistics
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
    age.append(col['age'])
    sex.append(col['sex'])
    bmi.append(col['bmi'])
    children.append(col['children'])
    smoker.append(col['smoker'])
    region.append(col['region'])
    charges.append(col['charges'])                               
#create dictionary for bmi sex
dict1 = {key:[bmi[idx]
       for idx in range(len(bmi)) if sex[idx]==key]
       for key in set(sex)}
#average bmi by sex
Fem = sum(item['female'] for item in dict1)
