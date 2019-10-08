from bioservices import UniProt
from chembl_webresource_client import *
from chembl_webresource_client.new_client import new_client
import xml.etree.ElementTree as ET
import requests
from xml.etree import ElementTree

targets = TargetResource()
u= UniProt()

res =u.search('(sphingolipid+OR+sphingomyelin+OR+glycosphingolipid)+AND+organism:9606 ', frmt='tab',columns='id, database(chembl)')
identifier = res[30:]
yeni = str(identifier)
lines = yeni.split('\n')
firstColumn = []
secondColumn = []
can=[]
for i in range(len(lines)):
  lineList = lines[i].split('\t')
  firstColumn.append(lineList[0])
  if len(lineList) == 2 : 
    secondColumn.append(lineList[1].strip(';'))
    t = targets.get(lineList[1].strip(';'))
    if t is not None:
        can.append(lineList[0])

smilchembl=[]
yeah =[]

for line in can:
  targets = new_client.target.filter(target_components__accession=line)
  activities = new_client.activity.filter(target_chembl_id__in=[target['target_chembl_id'] for target in targets])
  for activity in activities:
   smilchembl.append(activity['canonical_smiles'])
   yeah.append(activity['molecule_chembl_id'])



f=open("monomer.txt","r")
lines=f.readlines()

monoid = []
mono = []
sim= []
CID=[]
cid = []

for line in lines:
  monoid.append(line.split()[0])


for line in lines:
  cid.append(line.split()[1])
updateerror=[]
IC50cuttoff = "1000";
for line in firstColumn:
 if line is not None:
  url = "http://bindingdb.org/axis2/services/BDBService/getLigandsByUniprots?uniprot=%s&cutoff={1000}&code=[012]&response=application" %line
  response = requests.get(url)
  root = ElementTree.fromstring(response.content)
  for monomer in root.iter('monomerid'):
    mn= monomer.text
    mono.append(mn)
    if mn in monoid:
     index=monoid.index(mn)
     if index is not None:
      CID.append(cid[index])
    else:
      updateerror.append(mn)
  for smile in root.iter('smile'):
    sm= smile.text
    sim.append(sm)

print sim
print len(smilchembl)
print len(sim)
count=0
for line in smilchembl:
  if line in sim:
     count= count+1
print count