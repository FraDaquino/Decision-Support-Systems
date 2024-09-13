# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 20:35:19 2022

@author: Francesco Daquino.
"""
import csv

# ------- Directory dove salvare i nuovi file -----
path="project_data/"
# ------- Input File import -------
answerdataset = open("answerdataset/answerdatacorrect.csv", "r")
metadata = open("answerdataset/subject_metadata.csv", "r")
# ------ Create input readers -----
answerdataset_ds = csv.reader(answerdataset, delimiter = ",")
metadata_ds = csv.reader(metadata, delimiter = ",")
## ------- Output File import -------
subject=open(path+"subject.csv", "w", newline='')
# ------ Create output readers -----
subject_writer=csv.writer(subject)
 # ------ Set per controllare i distinti -----
subject_set= set()
# ----- Flag per controllare se stiamo leggendo l'header -----
first= True
is_header = True

# ----- inizializzazione dizionari vuoti  -----
sub_diz={}
diz_lev={}

def create_header(row):
    subject_header=["subjectid", "description"]
    subject_writer.writerow(subject_header)  

"""
La funzione pulisci il subjectid in input eliminando spazi e caratteri superflui,
e restituisce i valori come lista.
"""
def clean_subjectid(subjectid):
    char=" []"
    new_subjectid=[]
    for i in range(len(char)):
        subjectid=subjectid.replace(char[i],"")
    new_subjectid=subjectid.split(",")
    return new_subjectid

"""
La funzione legge la lista di valori pulita e li ordina per livello di materia.
"""
def ordina_subjectid(subjectid): 
    lista_finale =[]
    livello_zero =[]
    livello_uno = []
    livello_due = []
    livello_tre = []
    for i in subjectid:
        if diz_lev[i] == "0":
            livello_zero.append(i)
        if diz_lev[i] == "1":
            livello_uno.append(i)
        if diz_lev[i] == "2":
            livello_due.append(i)
        if diz_lev[i] == "3":
            livello_tre.append(i)
        lista_finale= livello_zero+livello_uno+livello_due+livello_tre
    return lista_finale

# ---------------------------------------------------------------------
#
# -------------- Creazione dizionario subjectid ----------------------
#
# ---------------------------------------------------------------------
for row in metadata_ds:
    if is_header  == True:        #controllo lettura header
        is_header = False
        continue 
    sub_diz[row[0]] = row[1]        # creazione dizionario {subjectid : subject_name} 
    diz_lev[row[0]] = row[3]        # creazione dizionario {subjectid : level} 
# ---------------------------------------------------------------------
#
# ------------------- Preparazione file finale -----------------------
#
# ---------------------------------------------------------------------
 
for row in answerdataset_ds:
    if  first:
        create_header(row)
        first = False
    else:  
        new_subjectid = clean_subjectid(row[13])               #ottengo subjectid come lista di valori stringa
        subjectid_ordinata = ordina_subjectid(new_subjectid)   #ottengo la lista ordinata per livello di materia
        
        if row[13] not in subject_set:      #controllo valori distinti di subjectid
            subject_set.add(row[13])    
            description=[]       
            for i in range(len(subjectid_ordinata)):               #itero quanti sono gli elementi nella lista subjectid
                description.append(sub_diz[subjectid_ordinata[i]]) #accesso al dizionario per recuperare la subject_name di riferimento
            subject_writer.writerow([row[13], description])        #scrittura file, e lascio row[13] perche deve coincidere con l'id in answer       
subject.close()