from bioservices import UniProt
from chembl_webresource_client import *
from chembl_webresource_client.new_client import new_client
import sys
from collections import defaultdict
from numpy import *
d = defaultdict(int)
targets = TargetResource()
u= UniProt()
""" the search funtion is used to extract the protein IDs from UniProt since the IDs are used as the
query set for data extraction from the chemical databases"""
res =u.search('(GO:0006665+OR+sphingolipid+OR+sphingomyelin+OR+glycosphingolipid)+AND+organism:9606', frmt='tab',columns='id, entry name, database(chembl)') 
identifier = res[42:] #42 is just choosen to get rid off the headers
yeni = str(identifier)
lines = yeni.split('\n')
un = []
name = []
chembl=[]
pro=[]

""" At this step, the information retrieved from the UniProt is saved as separate columns
depending on the info it has. For instance, after splitting the lines, the first entry is the ID, mid one
is protein short name and the third one is ChEMBL ID. All of them are saved as separate arrays to use at
the next step"""

for i in range(len(lines)):
  lineList = lines[i].split('\t')
  if len(lineList) == 3:
   un.append(lineList[0])
   name.append(lineList[1])
   if len(lineList[2]) is not 0 :
     t=targets.get(lineList[2].strip(';'))
     if t is not None:
         pro.append(lineList[0])

smil=[]
chem =[]
unp=[]
ac=[]

"""In this step, all the standard values are collected; and the list of them is in a file called
standvalue.txt"""
f=open("standvalue.txt","w")
for i in range(len(pro)):
  targets = new_client.target.filter(target_uniprot=pro[i])
  activities = new_client.activity.filter(target_chembl=[target['target_chembl_id'] for target in targets])
  for activity in activities:
     act=activity['standard_value']
     if act is not None:
         ac.append(act)
         print>>f,act

""" This standard values are counted for the frequency distribution."""
values=[]
g=open("standvalue.txt","r")
lines=g.readlines()
for line in lines:
    de=line.split()
    for j in de:
        d[j] += 1
        if j not in values:
            values.append(float(j))

frequency=[]
for line in values:
    frequency.append(float(d[float(line)]/2))

"""As the final step, standard values are printed versus their frequencies"""

import matplotlib.pyplot as plt
plt.scatter(values,frequency)
plt.ylabel("Frequencies")
plt.xlabel("Standard Values")
plt.axis([0,100050,0,1200]) # these parameters are changeable.
plt.show()

