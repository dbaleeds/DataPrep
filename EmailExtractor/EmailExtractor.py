import pandas as pd
from pathlib import Path

data = pd.read_csv("EmailExtractor/Users.csv",sep='\t',encoding='utf8',header=(0))

email_list = []
email_list2 = []
email_exempt = ['<>','zz_admin@company.com','admin@company.com']

for index, row in data.iterrows():
  email_list= email_list + (row['Users'].lower().split(';'))

for i in email_list:
  if i.strip() not in email_list2:
    email_list2.append(i.strip())

for exempt in email_exempt:
  if exempt in email_list2:
    email_list2.remove(exempt)

 
print(email_list2)