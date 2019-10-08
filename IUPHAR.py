from bioservices.uniprot import UniProt
import requests, json
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
u = UniProt()
 
res = u.search('sphingolipid_metabolism+AND+organism:9606', frmt='tab',columns='id')
identifiers = res.strip().split()[1:]
#hey = open('iuphar.txt','w')
for line in identifiers:
  url = "http://www.guidetopharmacology.org/services/targets?accession=%s&database=UniProt/XML" %line
  response = requests.get(url)
  t = response.status_code
  r=response.content
  if len(r) is not 0:
    t=r.find('targetId')
    a = r[t+12]+r[t+13]+r[t+14]+r[t+15]
    url = "http://www.guidetopharmacology.org/services/targets/%s/rankOrder" %a
    response = requests.get(url)
    T=response.content
    if len(T) is not 0:
       s=T.find('id=')
       oh = T[s+3]+T[s+4]+T[s+5]+T[s+6]
       url= "http://www.guidetopharmacology.org/services/ligands/%s/structure" %oh
       response = requests.get(url)
       ligand=response.content
       key=ligand.find('"smiles" :')+len('"smiles" :')
       for i in range(30):
         print ligand[key+i],
       
 

    
"""
  print t
  if t is 200:
     print >> hey,response.content
"""  