import pandas as pd

data = {'Name':['Naruto', 'Luffy', 'Zero2', 'Sayu','Kira','Hinata'],
        'Age':[15, 21, 19, 18,28,24]}
df = pd.DataFrame(data)
print(df)
print()
age_group=[15,20,25,30,35]
age_type=['Teen','Adult','Senior','Manager']
df['age_Groups']=pd.cut(df['Age'],bins=age_group,labels=age_type,right=False)

print(df)