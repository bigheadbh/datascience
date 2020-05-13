import csv
import matplotlib.pyplot as plt
import numpy as np 
import datetime
from xml.dom import minidom

#imprime o histograma
def print_data():
    with open('data', 'r') as arquivo:
        records = [n for n in arquivo]
        data = list()
        for record in records:
            record = record.rstrip("\n")
            data.append(float(record.split(" ")[2]))
            #print(record.split(" ")[2])
    fig, ax = plt.subplots(figsize =(10, 7)) 
    ax.hist(data, bins = 20)
    plt.savefig('histograma.png')

#processa os dados do xml
def get_heath_rate(filename):
    xmldoc = minidom.parse(filename)
    itemlist = xmldoc.getElementsByTagName('Record')
    for s in itemlist:
        if(s.getAttribute('type') == 'HKQuantityTypeIdentifierHeartRate'):
            print(s.getAttribute('creationDate').split(' ')[0:2], s.getAttribute('value'))


if __name__ == "__main__":
    #get_heath_rate('./data-34y.xml')
    print_data()

