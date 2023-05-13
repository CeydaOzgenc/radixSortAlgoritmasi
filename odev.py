import cProfile
import math
def dosyaAl(dosya):
    txt = open(dosya, "r")
    liste = txt.read()
    liste = liste.split("\n")
    liste.pop()
    cikti = ondaliktancevirme(liste)
    print(cikti)
def maxbasamak(liste):
    max=len(str(liste[0]))
    for i in range(1,len(liste)):
        if(len(str(liste[i]))>max):
            max=len(str(liste[i]))
    return max
def countingSort(liste,decimal):
    say=[0]*(10)
    cikti=[0]*(len(liste))
    for x in range(len(liste)):
        index = liste[x] // decimal
        say[index % 10]+=1 
    for y in range (1,10):
        say[y]=say[y]+say[y-1]
    i=len(liste)-1
    while i>=0:
        index = liste[i]//decimal
        cikti[say[index % 10] - 1] = liste[i]
        say[index % 10] -=1
        i-=1
    for z in range(0,len(liste)):
        liste[z] = cikti[z]
def ondaliktancevirme(liste):
    basamak=[]
    for i in range(len(liste)):
        liste[i]=float(liste[i])
        listeparca=str(liste[i]).split(".")
        basamak.append(listeparca[1])
    virgul=maxbasamak(basamak)
    sonuc=math.pow(10,virgul)
    for i in range(len(liste)):
        liste[i]=int(liste[i]*sonuc)
    sonuc = radixSort(liste,sonuc)
    return sonuc
def radixSort(liste,bol):
    maxsay=math.pow(10,maxbasamak(liste))
    decimal=1
    while maxsay/decimal>1:
        countingSort(liste,decimal)
        decimal*=10
    for i in range(len(liste)):
        liste[i]=float(liste[i]/bol)
    return liste
#dosyaAl("10lukliste.txt")
#dosyaAl("100lükliste.txt")
#dosyaAl("100000likliste.txt")
cProfile.run('dosyaAl("100000likliste.txt")')

