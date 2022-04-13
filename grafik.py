import matplotlib.pyplot as plt
import json
from istatistik import ceyrekAralikBul, medyanBul
 

f = open('data.json')
data = json.load(f)
fiyatlar = []
for urun in data:
    fiyatlar.append(int(urun['fiyat']))


urunSiralamasi = [x for x in range(len(fiyatlar))]
def graph1(urunSiralamasi):
    plt.scatter(urunSiralamasi, fiyatlar)
    plt.show()
    
def graph2():
    data = [min(fiyatlar) , ceyrekAralikBul(fiyatlar)[0] , medyanBul(fiyatlar) , ceyrekAralikBul(fiyatlar)[1], max(fiyatlar)]
    fig = plt.figure(figsize =(10, 7))
    plt.boxplot(data)
    plt.show()
def graph3():
    plt.style.use('ggplot')
    plt.hist(fiyatlar, bins=10)
    plt.show()
        
