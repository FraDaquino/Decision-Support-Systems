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
organization = open("project_data/organization.csv", "r")
date = open("project_data/date.csv", "r")

# ------ Create input readers -----
answerdataset_ds = csv.reader(answerdataset, delimiter = ",")
organization_ds = csv.reader(organization, delimiter = ",")
date_ds = csv.reader(date, delimiter = ",")

# ------- Output File import -------
answers=open(path+"answers.csv", "w", newline='')
# ------ Create output readers -----
answers_writer=csv.writer(answers)

 # ------ Set per controllare i distinti -----
answers_set = set() 

# ----- Flag per controllare se stiamo leggendo l'header -----
first = True
is_header1 = True
is_header2 = True
# ----- inizializzazione dizionari vuoti  -----
org_diz={}
date_diz ={}

def create_header(row):
    answers_header = ["answerid", "questionid", "userid", "organizationid", "dateid", "subjectid", "answer_value", "correct_answer","iscorrect", "confidence"]
    answers_writer.writerow(answers_header)

# ---------------------------------------------------------------------
#
# -------------- Creazione dizionari organization e date---------------
#
# --------------------------------------------------------------------- 
for row in organization_ds:  
    if is_header1  == True:
        is_header1 = False
        continue 
    org_diz[row[1]+row[2]+row[3]] = row[0]  # {(groupid+quizid+schemeofworkid) : organizationid}
    

for row in date_ds:
    if is_header2  == True:
        is_header2 = False
        continue 
    date_diz[row[1]] = row[0]  #   {(dateanswered) : dateid} 
     
# ---------------------------------------------------------------------
#
# ------------------- Preparazione file finale -----------------------
#
# ---------------------------------------------------------------------   

for row in answerdataset_ds:     #lettura answerdatacorrect
    if  first:
        # First create header
        create_header(row)        #creazione dell' header 
        first = False
    else:    
        if row[2] not in answers_set:   #controllo valori distinti di answerid
            answers_set.add(row[2])
            organizationid = org_diz[row[10]+row[11]+row[12]]    #accesso al dizionario per recuperare organizationid 
            date_answered = row[8]
            dateid = date_diz[date_answered[0:10]]  #accesso al dizionario per recuperare la date id,eliminando ore e minuti dalla data di risposta
        if row[3] == row[4]:    #creazione variabile iscorrect tramite confronto answer_value e correct_answer
            iscorrect = 1     
        else:
            iscorrect = 0
        answers_writer.writerow([row[2],row[0], row[1], organizationid , dateid, row[13], row[4], row[3], iscorrect , row[9]]) #scritture righe
answers.close()