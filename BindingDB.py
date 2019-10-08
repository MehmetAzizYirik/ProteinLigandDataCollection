""" Since BindingDB has its own monomer IDs, all IDs are converted to PubChem CIDs. For that, the list of all the identifier
mappings from monomer ID to PubChem IDs is downloaded from BindingDB webpage given below. That the file called monomer.txt
is used in the code. Thus, used need to download the updated list, then use it in our code.
(https://www.bindingdb.org/bind/chemsearch/marvin/SDFdownload.jsp?all_download=yes)"""

from bioservices.uniprot import UniProt
import requests
from xml.etree import ElementTree
u = UniProt()
 
res = u.search('(sphingolipid+OR+sphingomyelin+OR+glycosphingolipid)+AND+organism:9606 ', frmt='tab',columns='id')
identifiers = res.strip().split()[1:]
#hey = open("bindingdb.txt","w")
f=open("monomer.txt","r")
lines=f.readlines()

monoid = []
mono = []
sim= []
CID=[]
cid = []

""" All the monomerIDs and their equivalent CIDs are saved as separate arrays"""

for line in lines:
  monoid.append(line.split()[0])


for line in lines:
  cid.append(line.split()[1])

IC50cuttoff = "1000" #IC50 threshold for the monomers

"""For the list of the UniProt IDs, compounds are extracted from BindingDB as a XML file. Then the file is parsed to collect
monomer IDs and their SMILES. Each monomer ID is converted to CID"""

for line in identifiers:
  url = "http://bindingdb.org/axis2/services/BDBService/getLigandsByUniprots?uniprot=%s&cutoff={1000}&code=[012]&response=application" %line
  response = requests.get(url)
  print response
  root = ElementTree.fromstring(response.content) 
  for monomer in root.iter('monomerid'):
    mn= monomer.text
    mono.append(mn)
    if mn in monoid:
     print mn 
     index=monoid.index(mn)
     if index is not None:
      print cid[index]
      CID.append(cid[index])
  for smile in root.iter('smile'):
    sm= smile.text
    sim.append(sm)

"""The list of the monomer IDs, their CIDs and SMILES are listed"""

for i in range(len(sim)):
    print mono[i]+"\t"+CID[i]+"\t"+sim[i]



