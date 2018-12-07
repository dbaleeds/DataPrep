# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:28:26 2018
@author: dbaleeds
A script to strip the ID column of a file, shufle the rows and re-append a ID. To ensure sensitive anonymous data sets rows are not in sequential order to minimise re-identification.
"""

import random
import pandas as pd
import csv

#1 - shuffle rows
with open("S:\Faculty-of-Medicine-and-Health\Research-Projects\LAPCD\Linked Data\Merged UK data\Jenni\Data prep\LAPCD data for PHE.csv","r") as ip:
    data=ip.readlines()

#split header and remaining lines, so header is not shuffled
header, rest=data[0], data[1:]

#shuffle lines
random.shuffle(rest)

#write shuffled lines with the header row
with open("S:\Faculty-of-Medicine-and-Health\Research-Projects\LAPCD\Linked Data\Merged UK data\Jenni\Data prep\LAPCD data for PHE_treatedv1.csv","w",newline='') as out:
  out.write(''.join([header]+rest))
  out.close()
    
#2 - remove ID column
  with open("S:\Faculty-of-Medicine-and-Health\Research-Projects\LAPCD\Linked Data\Merged UK data\Jenni\Data prep\LAPCD data for PHE_treatedv1.csv", "r") as file_in:
      with open("S:\Faculty-of-Medicine-and-Health\Research-Projects\LAPCD\Linked Data\Merged UK data\Jenni\Data prep\LAPCD data for PHE_treatedv2.csv", "w", newline='') as file_out:
        writer = csv.writer(file_out)
#iterate through all rows starting from position 1 (leaving out column 0 - id)
        for row in csv.reader(file_in):
          writer.writerow(row[1:])          
      file_out.close()    
  file_in.close()          
          
#3 - add new ID column      
with open('S:\Faculty-of-Medicine-and-Health\Research-Projects\LAPCD\Linked Data\Merged UK data\Jenni\Data prep\LAPCD data for PHE_treatedv2.csv') as inp, open('S:\Faculty-of-Medicine-and-Health\Research-Projects\LAPCD\Linked Data\Merged UK data\Jenni\Data prep\LAPCD data for PHE_treatedv3.csv', 'w', newline='') as out:
    reader = csv.reader(inp)
    writer = csv.writer(out, delimiter=',')
    #No need to use `insert(), `append()` simply use `+` to concatenate two lists.
    writer.writerow(['id'] + next(reader))
    #Iterate over enumerate object of reader and pass the starting index as 1.
    writer.writerows([i] + row for i, row in enumerate(reader, 1))
inp.close()
out.close()   

    
    