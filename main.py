import csv
import matplotlib.pyplot as plt
import numpy as np 
import datetime
from xml.dom import minidom

#imprime o histograma
def get_histograma():
    with open('data', 'r') as arquivo:
        records = [n for n in arquivo]
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
    plt.savefig('histograma.png')


#imprime a distribuicao cumulativa CDF
def get_CDF():
    with open('data', 'r') as arquivo:
        records = [n for n in arquivo]
        data = list()
        for record in records:
            record = record.rstrip("\n")
            data.append(float(record.split(" ")[2]))
    
    fig, ax = plt.subplots(figsize =(10, 7)) 
    #ax.hist(data, bins=20, cumulative=True, label='CDF', alpha=0.55, color='purple')
    ax.hist(data, bins=20, density=True, histtype='step', cumulative=True)

    #adding extra features     
    plt.xlabel("heartbeat frequency") 
    plt.ylabel("% occurrences") 
    plt.title('CDF for heart rate') 
    plt.savefig('CDF.png')

#processa os dados do xml
def get_heath_rate(filename):
    xmldoc = minidom.parse(filename)
    itemlist = xmldoc.getElementsByTagName('Record')
    for s in itemlist:
        if(s.getAttribute('type') == 'HKQuantityTypeIdentifierHeartRate'):
            print(s.getAttribute('creationDate').split(' ')[0:2], s.getAttribute('value'))


if __name__ == "__main__":
    #get_heath_rate('./data-34y.xml')
    #get_histograma()
    #get_CDF()


