# Module Fonction
# Librairie Brunel Alexis 
from math import sqrt
def Max(liste,dec=0):
    p=0
    for i in range(dec+1,len(liste)):
        if liste[i]>liste[p]:
            p=i
    return liste[p]

def Min(liste,dec=0):
    p=dec
    for i in range(dec+1,len(liste)):
        if liste[i]<liste[p]:
            p=i
    return p

def echange(liste,i,j):
    liste[i],liste[j]=liste[j],liste[i]
    return liste


def moyenne(L) :
	somme=0
	for i in range (len(L)):
		somme=somme+L[i]
	moy=somme/len(L)
	return moy

def ecartType(L) :
	moy=moyenne(L)
	x=[]
	for i in range (len(L)) :
		x.append((L[i]-moy)**2)
	y=moyenne(x)
	sigma=sqrt(y)
	return sigma

def pourcentage (v,x):
	por=v/x*100
	return por

def covariance(x,y):
    moy1=moyene(x)
    moy2=moyene(y)
    result=0
    for index,val in enumerate(x):
    #index=index  de la liste ,val =valeur a l'indice
        result+=(val-moy1)*(y[index]-moy2)
        result=result/len(x)
        return result




