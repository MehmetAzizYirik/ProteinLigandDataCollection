from bioservices import UniProt
from bioservices import PDB
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
a = PDB()
u = UniProt()
pdb = [ ]
ids = [ ]
chem = [ ]
smil = [ ]

""" By the keywords, equivalent PDB IDs are extracted if proteins have for their UniProt IDs."""

ress=u.search('(GO:0006665+OR+sphingolipid+OR+sphingomyelin+OR+glycosphingolipid)+AND+organism:9606', frmt='tab', columns='database(pdb)')
identifierss = ress.split(';')[1:]  # [1:] gets rid of the header

""" The PDB IDs are saved as an array"""

for line in identifierss:
    t = line.strip()
    pdb.append(t)

""" For each protein, their ligand information is extracted from PDB via BioServices' function
called get_ligands whose output is an XML file. These files are parsed to list structre IDs
chemical IDs and SMILES as separate arrays."""

for i in range(len(pdb)-1): 
    root = ET.fromstring(a.get_ligands(pdb[i]))
    for child in root :
      for ligan in child.iter('ligand'):
       chem.append(ligan.get('chemicalID'))
       ids.append(ligan.get('structureId'))
      for smiles in child.iter('smiles') :
       smil.append(smiles.text)

""" These PDB IDs, Chemical IDs, and SMILES are listed"""

for i in range(len(ids)):
  print ids[i] + '\t' + chem[i] + '\t' + smil[i]
