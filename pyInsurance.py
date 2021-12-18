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
#create dictionarie for bmi sex
dict = dict(zip(bmi, sex))
print(dict)