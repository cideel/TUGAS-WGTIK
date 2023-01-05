
def bacaData():
    file = open("tubes.txt","r")

    teks = file.readline().replace("\n","")
    while teks !="":
        print(teks)
        teks = file.readline().replace("\n","")
    file.close()
def point(menang,seri):
    hasil = (menang*3) + (seri*1)
    return hasil




#main

#dictionary
data = {'Bhayangkara' : ["Bhayangkara",46,12],'Persib':["Persib",54,15],"Arema":["Arema",38,21]
              ,"Bali":["Bali",46,20],"PSIS":["PSIS",43,19],"Persebaya":["Persebaya",54,-1],"BornoeFC":["BorneoFC",53,4],
              "Persija":["Persija",56,-2],"Persita":["Persita",65,18],"PSS":["PSS",50,17],"PSM":["PSM",28,15],"MaduraUnited":["MaduraUnited",49,14],
              "Persikabo":["Persikabo",57,2],"Persik":["Persik",69,-5],"Persela":["Persela",60,7],"BaritoPutera":["BaritoPutera",43,13],
              "Persipura":["Persipura",59,23],"Persija":["Persiraja",70,15]}

value_dict = data.values()
value_list = list(value_dict)
data_klub = [item[0] for item in value_list]
data_point = [item[1] for item in value_list]


def cari():
    x = int(input("Masukkan Poin : "))
    car_point = [i for i in data_point if i < x]
    for i in car_point:
        letak = data_point.index(i)
        letak_klub = data_klub[letak]
        print(letak_klub)






#mencari juara liga
def juara_liga():
    poin_tinggi = max(data_point)
    #pengecekkan jika ada point sama
    poin_sama = data_point.count(poin_tinggi)
    if poin_sama == 1:
        index = data_point.index(poin_tinggi)
        klub_juara = data_klub[index]
        return klub_juara
    else:
     return false
#cari point
print(bacaData())

print(juara_liga())
cari()





