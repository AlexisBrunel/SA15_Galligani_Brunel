# Code pour SAE 15
from lxml import etree
import module as stat
import requests
import time
from time import sleep
import os
parkings=["FR_MTP_ANTI","FR_MTP_COME","FR_MTP_CORU","FR_MTP_EURO","FR_MTP_FOCH"
,"FR_MTP_GAMB","FR_MTP_GARE","FR_MTP_TRIA","FR_MTP_ARCT","FR_MTP_PITO"
,"FR_MTP_CIRC","FR_MTP_SABI","FR_MTP_GARC","FR_MTP_SABL","FR_MTP_MOSS"
,"FR_MTP_MEDC","FR_MTP_OCCI","FR_CAS_VICA","FR_MTP_GA109"
,"FR_MTP_GA250","FR_CAS_CDGA","FR_MTP_ARCE",'FR_MTP_POLY',"FR_STJ_SJLC"]
def recupparking(v):

    f1=open("dataparking.txt","w",encoding='utf8')
    
    for i in range(0,50):


        total_place=0#Pour pourcentage total 
        total_libre=0#Pour pourcentage total,libre
        for w in (v):
            
            a="https://data.montpellier3m.fr/sites/default/files/ressources/"+w+".xml"  #Pour récup les liens de chaque parkings sur le site de montpellier             
            print(a)
            response=requests.get(a)
            f2=open(w,"w", encoding='utf8')#Ouvrir dans des fichier du noms de chaque Parking 
            f2.write(response.text)
            f2.close()
            tree = etree.parse(w)
            os.remove(w)
            f2=open(w+".txt",'w',encoding='utf-8')
            for name in tree.xpath("Name"):#Récuper les Noms de chaque parking (du site )
                print('Nom du parking :',name.text)
                f2.write('Nom du parking :'+name.text+"\n")
            for tot in tree.xpath("Total"):   #Récuper les Nombres de places de chaque parking (du site )
                print('Nombre total de places totales :',tot.text)
                f2.write('Nombre total de places totales :'+tot.text+"\n")  
                k=tot.text
                total_place+=int(k)       
            for fr in tree.xpath("Free"):#Récuper les Nombres de places libres de chaque parking (du site )
                print('Nombre de places libres :',fr.text)
                f2.write('Nombre de places libres :'+fr.text+"\n")
                j=fr.text
                total_libre+=int(j)
            o=stat.pourcentage(int(j),int(k))
            print("Pourcentage de places libres : "+str(round(o, 2))+"%")
            f2.write("Pourcentage de places libres : "+str(round(o, 2))+"%")
            f2.close()
        #Cacule avec le module du pourcentage de tout les place libre 
        m=stat.pourcentage(total_libre , total_place)
        print ("Le pourcentage total de places occupés de tout les parkings réunis est de :",round(m,2),"%")
        #Pourcentage de place libre pour tout les parkigs (arrondi au centiéme pres)
        f1.write(str(i)+" "+str(round(m, 2))+"\n")
        sleep(60) 
         
    f1.close()
    
   
recupparking(parkings)