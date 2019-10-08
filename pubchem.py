from bioservices import UniProt
import requests

u= UniProt()
CID=[]
a=[]
b=[]
name=[]
human=[]
p=open("respubchem.txt","w")
f=open("humanpubchem.txt","r")
lines=f.readlines()

for line in lines:
    c=line.split('\t')
    if len(c)>2:
      if "CID" not in c[3]:
          CID.append(c[3])

"""
for line in lines:
    c=line.split('\t')
    if len(c)>2:
      if "Target" not in c[9]:
          name.append(c[9])
  
for line in lines:
    c=line.split('\t')
    if len(c)>2:
      if "Target" not in c[9]:         
          if c[9] not in a: #for the reputation, we need to save them as singular one in another array
            a.append(c[9])
            res=u.search(c[9],frmt="tab", columns="entry name")
            for line in res.split():
                if "HUMAN" in line:
                 if len(c[9])>0:              
                    if  c[9][len(c[9])-1] is 1 or 2:
                     print c[9]
                     break
"""

hop=[]
res=[]
smil=[]
for i in range(len(CID)):
   url= "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/%s/property/IsomericSMILES/CSV" %CID[i]
   response = requests.get(url)
   t=(response.content)
   print>>p, t
   hop.append(t)
   print len(hop)

"""
   res.append(t)
   l=t.split( )[1]
   can=l.split(",")
   if len(can) is 2:
     of=(can[1].strip('"'))
     smil.append(of)
     print CID[i], of
     
 
   if len(sml)>0:
       smil.append(sml)

   smil.append(sml)
   cid= l.split(",")[0]
   ind=CID.index(cid)
# print name[ind], cid, sml

print len(smil)
"""