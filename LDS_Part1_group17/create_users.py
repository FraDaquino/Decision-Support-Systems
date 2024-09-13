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
geography = open("project_data/geography.csv", "r")
date = open("project_data/date.csv", "r")

# ------ Create input readers ----- LEGGO GEOGRAPHY E DATE PER CREARMI I DIZIONARI
answerdataset_ds = csv.reader(answerdataset, delimiter = ",")
geography_ds = csv.reader(geography, delimiter = ",")
date_ds = csv.reader(date, delimiter = ",")

## ------- Output File import -------
users=open(path+"users.csv", "w", newline='')
# ------ Create output readers -----
users_writer=csv.writer(users)

 # ------ Set per controllare i distinti -----
users_set=set()
# ----- Flag per controllare se stiamo leggendo l'header -----
first = True
is_header1 = True
is_header2 = True
# ----- inizializzazione dizionari vuoti  -----
geo_diz={}
date_diz={}

def create_header(row):
    users_header=["userid", "dateofbirthid" ,"geoid", "gender"]
    users_writer.writerow(users_header)
# ---------------------------------------------------------------------
#
# -------------- Creazione dizionari geography e date---------------
#
# --------------------------------------------------------------------- 
for row in geography_ds:   
    if is_header1  == True:
        is_header1 = False
        continue 
    geo_diz[row[1]] = row[0]   # creazione dizionario {geoid : region} 

for row in date_ds:
    if is_header2  == True:
        is_header2 = False
        continue 
    date_diz[row[1]] = row[0]   # creazione dizionario {dateid : date} 
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
        if row[1] not in users_set:    #controllo valori distinti di userid
            users_set.add(row[1])  
            geoid_user = geo_diz[row[15]]      #accesso al dizionario per recuperare la geoid
            dateofbirthid = date_diz[row[6]]   #accesso al dizionario per recuperare la dateofbirthid
            users_writer.writerow([row[1], dateofbirthid, geoid_user, row[5]])
users.close()