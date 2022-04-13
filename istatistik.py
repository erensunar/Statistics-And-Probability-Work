import json
f = open('data.json')

data = json.load(f)
fiyatlar = []


for urun in data:
    fiyatlar.append(int(urun['fiyat']))


def ortalamaBul(fiyatlar):
    toplam = 0
    for fiyat in fiyatlar:
        toplam = toplam + fiyat

    return toplam / len(fiyatlar)



def medyanBul(fiyatlar):
    siraliFiyatlar = sorted(fiyatlar)
    veriAdedi = len(siraliFiyatlar)
    if (veriAdedi % 2) == 1:
        return siraliFiyatlar[veriAdedi // 2]
    else:
        i = veriAdedi // 2
        return (siraliFiyatlar[i + 1] + siraliFiyatlar[i]) / 2

def modBul(fiyatlar):
    tekrarSayisi = 0
    mod = 0
    fiyatlar = sorted(fiyatlar)
    for fiyat in fiyatlar:
        bulunanAdet = fiyatlar.count(fiyat)
        if bulunanAdet > tekrarSayisi:
            tekrarSayisi = bulunanAdet
            mod = fiyat
    return mod

def aralikBul(fiyatlar):
    maxDeger = max(fiyatlar)
    minDeger = min(fiyatlar)
    aralik = maxDeger - minDeger
    return aralik

def ortaAralikBul(fiyatlar):
    aralik = aralikBul(fiyatlar)
    return aralik / 2

def ceyrekAralikBul(fiyatlar):
    aralik = aralikBul(fiyatlar)
    ilkCeyrekAralik = aralik * 0.25
    sonCeyrekAralik = aralik * 0.75
    return ilkCeyrekAralik, sonCeyrekAralik


def standartSapmaBul(fiyatlar):
    ortalama = ortalamaBul(fiyatlar)
    standartSapma = 0
    for fiyat in fiyatlar:
        deger = (fiyat - ortalama) ** 2
        standartSapma += deger

    standartSapma = standartSapma / (len(fiyatlar) - 1)
    standartSapma = standartSapma ** 0.5
    return standartSapma

def varyansBul(fiyatlar):
    standartSapma = standartSapmaBul(fiyatlar)
    varyans = standartSapma ** 2
    return varyans


def ortalamaMutlakSapmaBul(fiyatlar):
    toplam = 0
    for fiyat in fiyatlar:
        ortalama = ortalamaBul(fiyatlar)
        deger = fiyat - ortalama
        if deger < 0:
            deger = deger * -1
        toplam = toplam + deger
    
    return toplam / len(fiyatlar)




print("Fiyatların ortalaması: ", str(ortalamaBul(fiyatlar)) +"\n" + "Fiyatların medyanı: " + str(medyanBul(fiyatlar)) + "\nFiyatların modu: "+ str(modBul(fiyatlar)))
print("Fiyatların aralığı: " + str(aralikBul(fiyatlar)), "\nFiyatların orta aralığını bul: " + str(ortaAralikBul(fiyatlar)))
print("Fiyatların ilk çeyrek aralığı: " + str(ceyrekAralikBul(fiyatlar)[0]))
print("Fiyatların son çeyrek aralığı: " + str(ceyrekAralikBul(fiyatlar)[1]))
print("Fiyatların standart sapması: " + str(standartSapmaBul(fiyatlar)))
print("Fiyatların varyansı: " + str(varyansBul(fiyatlar)))
print("Fiyatların ortalama mutlak sapma değeri: " + str(ortalamaMutlakSapmaBul(fiyatlar)))
f.close()