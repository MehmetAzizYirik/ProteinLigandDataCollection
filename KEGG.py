from bioservices.uniprot import UniProt
import requests, json
from xml.etree import ElementTree

url = "http://rest.kegg.jp/find/pathway/sphingolipid"
response = requests.get(url)
t=(response.content).split()
lines=[]

for line in t:
    if "path:" in line:
        mapid=line.strip("path:")
        url = "http://rest.kegg.jp/link/cpd/%s" %mapid
        response = requests.get(url)
        t=(response.content).split()
        if t is not None:
            for line in t:
                if "cpd:" in line:
                    url = "http://rest.kegg.jp/get/%s" %line
                    response = requests.get(url)
                    t=(response.content).split()
                    for line in t:
                        lines.append(line)
for i in range(len(lines)-1):
    if "PubChem:" in lines[i]:
        url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/%s/property/IsomericSMILES/CSV" %lines[i+1]
        response = requests.get(url)
        t=(response.content).split()
        print t


"""
res= t.split("\t")

for line in res:
  print line
      

ar=[]
t=h.split('\t')

for line in t:
    ar.append(line)
i=0
for line in ar:
    i=i+1
    print i,line
    


array=[]
for line in t:
    array.append(line)
for i in range(len(array)):
    a=array[i].find("sphingolipid")
    if a >0:
        print array[i+1]
"""
