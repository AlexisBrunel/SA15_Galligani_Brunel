from lxml import etree
import module as stat
import requests
import time
from time import sleep
import os
#Récuperer les informations sur les parkings a velo
def recupvelo ():
        total=0
        total_libre=0
        response=(requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")).text
        f1=open('velo.xml','w',encoding='utf8')
        f1.write(response)
        f1.close()
        f2=open("Resultat.txt",'w',encoding='utf8')
        tree=etree.parse('velo.xml')
        f1=open("datavelo.txt", "w",encoding="utf8")
        for i in range(0, 50):    
            for si in tree.xpath('/vcs/sl/si'):
                nom=si.get('na')
                place_libre=si.get('fr')
                place_libre=int(place_libre)
                place_total=si.get('to')
                place_total=int(place_total)
                pourcent=stat.pourcentage(place_libre, place_total)
                total_libre+=place_libre
                total+=place_total
                f2.write(nom+"\n")
                f2.write(" Place libre : "+str(place_libre)+"\n")
                f2.write(" Place total : "+str(place_total)+"\n")
                f2.write(" Pourcentage place libre : "+str(round(pourcent, 2))+"%\n")
                f2.write("\n")
            m=stat.pourcentage(total_libre, total)
            f1.write(str(i)+" "+str(round(m, 2))+"\n")
            sleep(60)
        f1.close()
        f2.close()
        os.remove('velo.xml')
    
recupvelo()

    
    


