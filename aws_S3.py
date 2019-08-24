"""Script de prueba para automatizar carga de archivos en S3"""

import pandas as pd 
import numpy as np
import os
import datetime 
import boto3

# Hora del servidor
hora=datetime.datetime.now()

# Nombre de la carpeta 
file_name=hora.strftime("%d-%b-%Y %H:%M") 

# Creamos ruta de la carpeta
ruta=os.getcwd()+'/'+file_name

# Creamos la carpeta dinamica
os.mkdir(os.getcwd()+'/'+file_name)  


#Cargamoslos documentos

data911=pd.read_csv('911.csv')
dataCollege=pd.read_csv('College_Data',sep=',')

# Movemos los archivos a la carpeta con nombre dinamico 

data911.to_excel(ruta+'/911.xlsx')
dataCollege.to_excel(ruta+'/College_data.xlsx')

# Zona de traslado de archivos a S3
s3 = boto3.resource("s3")
BUCKET = "alex-test-autos3"

s3.Bucket(BUCKET).upload_file(file_name+'/911.xlsx',file_name+'/911.xlsx')
s3.Bucket(BUCKET).upload_file(file_name+'/College_data.xlsx',file_name+'/College_data.xlsx')
