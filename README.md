# ProteinLigandDataCollection

Copyright 2019 Mehmet Aziz Yirik

## Introduction

Source code is written in Python (version 2.7);moreover, it includes functions of some python packages namely BioServices, Chembl Webresource Client,requests and xml.etree. Therefore, users firstly should obtain these packages by applying via "pip" comment of Python. For instance, to install bioservices, typing "pip install bioservices" to the command prompt is enough.

These package includes many functions to collect protein ligand interaction information from different databases such as ChEMBL, BindingDB, and PDB. To collect the data from these databases via these functions, the only requirement is to type a keyword to search at the search boxes of these functions. 

The repository provides data collection scripts for protein-ligand interactions. The scripts were from my master thesis (2017). The thesis can be accessed from the link: http://seyhan.library.boun.edu.tr/record=b1841056~S5

## Input

For example, by typing "insulin" into the search box of CHEMBL function, the protein-ligand interaction information can be collected from ChEMBL. 

## Output

The output of this function is suitable to use as an input for Ligand Centric Network Models package. These output includes three columns; orderly, protein IDs, ligand IDs and SMILES strings. First lines of these insulin output is given below. 

AKT1_HUMAN	CHEMBL2368946	CCCCCCCCCCCCCCCCCCOC[C@H](COP(=O)(O)O[C@@H]1[C@H](O)C[C@@H](O)[C@H](O)[C@@H]1O)n2ccnc2
AKT1_HUMAN	CHEMBL2368944	CCCCCCCCCCCCCCCC(=O)C[C@H](COP(=O)(O)O[C@@H]1[C@H](O)C[C@@H](O)[C@H](O)[C@@H]1O)C(=O)CCCCCCCCCCCCCCC
AKT1_HUMAN	CHEMBL2368948	CCCCCCCCCCCCCCCCCCOC[C@H](COP(=O)(O)O[C@@H]1[C@H](O)C[C@@H](O)[C@H](O)[C@@H]1O)OC
AKT1_HUMAN	CHEMBL2368945	CCCCCCCCCCCCCCCCCCOC[C@H](COP(=O)(O)O[C@H]1[C@@H](O)[C@@H](O)[C@H](O)[C@H](CO)[C@H]1O)n2ccnc2
AKT1_HUMAN	CHEMBL2368953	CCCCCCCCCCCCCCCCCCOC[C@H](COC(=O)O[C@H]1[C@@H](O)[C@@H](O)[C@H](O)[C@H](CO)[C@H]1O)OC
AKT1_HUMAN	CHEMBL2368954	CCCCCCCCCCCCCCCCCCOC[C@H](COC(=O)O[C@H]1[C@@H](O)[C@@H](O)[C@H](O)[C@H](CO)[C@@H]1O)n2ccnc2
AKT1_HUMAN	CHEMBL2368947	CCCCCCCCCCCCCCCCCCOC[C@H](COP(=O)(O)O[C@H]1[C@@H](O)[C@@H](O)[C@H](O)[C@H](CO)[C@H]1O)OC
AKT1_HUMAN	CHEMBL388978	CN[C@@H]1C[C@H]2O[C@@](C)([C@@H]1OC)n3c4ccccc4c5c6CNC(=O)c6c7c8ccccc8n2c7c35
AKT1_HUMAN	CHEMBL200906	CN1C(=O)C(C(=O)Nc2nncs2)c3cc4occc4cc13
AKT1_HUMAN	CHEMBL414139	COc1cc2c(Nc3ccc(Oc4ccccc4)cc3)c(cnc2cc1OCCCN5CCOCC5)C#N
AKT1_HUMAN	CHEMBL318804	COc1cc2c(Nc3ccc(Sc4nccn4C)c(Cl)c3)c(cnc2cc1OCCCN5CCOCC5)C#N
AKT1_HUMAN	CHEMBL260417	Oc1ccc(cc1)c2nc3[nH]nc(NC(=O)C4CC4)c3cc2Br


## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/MehmetAzizYirik/ProteinLigandDataCollection/blob/master/LICENSE) file for details

## Authors

 - Mehmet Aziz Yirik - [MehmetAzizYirik](https://github.com/MehmetAzizYirik)
 
