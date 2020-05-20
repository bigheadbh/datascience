import csv
import matplotlib.pyplot as plt
import numpy as np 
import datetime
from xml.dom import minidom

#imprime o histograma
def get_histograma(records):
    data = list()
    for record in records:
        record = record.rstrip("\n")
        data.append(float(record.split(" ")[2]))
        #print(record.split(" ")[2])
    fig, ax = plt.subplots(figsize =(10, 7)) 
    ax.hist(data, bins = 20)
    
    #adding extra features     
    plt.xlabel("heartbeat frequency") 
    plt.ylabel("# occurrences") 
    plt.title('histogram for heart rate') 
    plt.savefig('../graficos/histograma.png')

#imprime a distribuicao cumulativa CDF
def get_CDF(records):
    data = list()
    for record in records:
        record = record.rstrip("\n")
        data.append(float(record.split(" ")[2]))
    
    fig, ax = plt.subplots(figsize =(10, 7)) 
    #ax.hist(data, bins=20, cumulative=True, label='CDF', alpha=0.55, color='purple')
    ax.hist(data, bins=50, density=True, histtype='step', cumulative=True)

    #adding extra features     
    plt.xlabel("heartbeat frequency") 
    plt.ylabel("% occurrences") 
    plt.title('CDF for heart rate') 
    plt.savefig('../graficos/CDF.png')

#processa os dados do xml
def get_heath_rate(filename):
    xmldoc = minidom.parse(filename)
    itemlist = xmldoc.getElementsByTagName('Record')
    for s in itemlist:
        if(s.getAttribute('type') == 'HKQuantityTypeIdentifierHeartRate'):
            print(s.getAttribute('creationDate').split(' ')[0:2], s.getAttribute('value'))


if __name__ == "__main__":
    #get_heath_rate('../base_de_dados/data-34y.xml')
    records = [n for n in open("../base_de_dados/data")]
    get_histograma(records)
    get_CDF(records)


