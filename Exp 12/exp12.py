import pandas as pd
data = {"Naruto":20,"Sasuke":23,"Sakura":17,"kakshi":27,"Zabuza":30,"Hashiram":47,"Madara":50}
df = pd.Series(data)

print(df[0])
c1=0
c2=0
c3=0
c4=0
for value in df.items():
    if df[value]<18:
        c1+=1
    elif df[value]>=18 and df[value]<25:
        c2+=1
    elif df[value]>=25 and df[value]<40:
        c3+=1
    elif df[value]>=40:
        c4+=1
    pass

print("Below 18: "+str(c1))
print (df)