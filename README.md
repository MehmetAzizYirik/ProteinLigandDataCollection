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

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/MehmetAzizYirik/ProteinLigandDataCollection/blob/master/LICENSE) file for details

## Authors

 - Mehmet Aziz Yirik - [MehmetAzizYirik](https://github.com/MehmetAzizYirik)
 
