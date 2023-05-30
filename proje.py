#elif tilki 
liste=[]                                      #salonu tutacak liste
for i in range(20):                           #salonun şeklini almasını sağlar
    liste.append(["|-|","|-|","|-|","|-|","|-|","|-|","|-|","|-|","|-|","|-|","|-|","|-|","|-|","|-|","|-|","|-|","|-|","|-|",
                  "|-|","|-|","|-|"])

dosya=open("indirim1.txt","r")
indirimbilgi=[]
dosyaicbilgi=[]
dizi=dosya.readlines()                        #dosyaki her satırı okuyup listeye atma
dosya.close()                                 #dosyayı kapama

for vb in dizi:
    indirimbilgi.append(vb.strip())           #dizikedi \n ifadelerini siler

for kj in indirimbilgi:
    dosyaicbilgi.append(kj.split("-"))        #indirimbilgi'den "-" haricindekiler liste yapar

for lf in range(len(dosyaicbilgi)):                   #dosyadaki M değerlerini 10 yapar
    for kl in range(len(dosyaicbilgi[lf])):
        if(dosyaicbilgi[lf][kl].__eq__("M")):
            dosyaicbilgi[lf][kl]="10"

netucretkategori=[0,0,0,0] #her kategorinin ayrı olarak cirosunu tutan liste
sayac6=0                   #indirim uygulanmadığındada bilet ve ücreti basmamızı sağlar

def ucretHesaplama(yt):
    oran=0             # uygulanacak indirim oranını tutan değişken
    indirim=0          # uygulanacak indirim değerini tutan değişken
    netucret=0         # indirim uygulanması ile elde edilen ücret
    indirimsizucret=0  # indirimin uygulanmadığı ücret
    if(b>=int(dosyaicbilgi[yt][1]) and b<=int(dosyaicbilgi[yt][2])):
        oran=int(dosyaicbilgi[yt][3])
        indirimsizucret=b*fiyat
        indirim=indirimsizucret*(oran/100)
        netucret=indirimsizucret-indirim
        netucretkategori[k-1]=netucretkategori[k-1]+netucret
        global sayac6
        sayac6=1
        print("bilet adedi:", b, "toplam tutar:", indirimsizucret, "yapılan indirim:", indirim, "net tutar:",netucret)
sayac4=0            #kategoride boş koltuk  kalmadığı durumda fiyat bilgisi basmamayı sağlayan sayaç

def kategori1(b):   #kategori 1 için bilet kesim işlemlerini yapan fonksiyon
    sayac=0        #kesilen bilet sayısını tutan sayaç
    e=0            #salon satır sayısı
    r=0            #salon sutun sayısı
    sayac2=0       #kategoride boş koltuk bulma sayacı
    lie=[]         #seçilen koltukların satır sayısını tutan liste
    lir=[]         #seçilen koltukların sütun sayısını tutan liste
    sayac3=0
    global sayac4
    sayac4=0
    sayac5=0

    for nm in range(5,15):
        if(liste[9][nm].__eq__("|x|")):
            sayac5=sayac5+1
    if(sayac5==10):
        print("\nbilet adedi 1. kategorideki boş koltuk adedini aşıyor.")
        print("rezervasyon yapılamadı")
        sayac3 = 1
        sayac4 = 1
        b=0

    for j in range(10):
        for z in range(5,15):
            if(liste[j][z].__eq__("|-|")):
                e=j
                r=z
                sayac2=1
                break
        if(sayac2==1):
            break

    while(b>0):
        b=b-1
        liste[e][r]="|x|"
        lie.append(e)         #seçilen koltuğun satır numarısını listeye atıyoruz
        lir.append(r)         #seçilen koltuğun sütun numarısını listeye atıyoruz
        r = r + 1
        if(b==0):
            break

        sayac=sayac+1
        if(r>14):
            r=5
            e=e+1
            if(e>9):
                print("\nbilet adedi 1. kategorideki boş koltuk adedini aşıyor.")
                print("rezervasyon yapılamadı")
                sayac3=1
                sayac4=1
                e=9
                r=14
                while(sayac>0):
                    liste[e][r]="|-|"
                    r=r-1
                    sayac=sayac-1
                    b=0

    if(sayac3==0):
        print("Reverze edilen koltuklar(sira-koltuk):", end=" ")
        for hj in range(len(lie)):
            print("{}-{}".format(lie[hj]+1, lir[hj]+1), end=" ")

    print("\n")

def kategori2(b):                        #kategori 2 için bilet kesim işlemlerini yapan fonksiyon
    e = 0
    r = 0
    sayac = 0
    sayac2 = 0
    lie = []
    lir = []
    sayac3 = 0
    global sayac4
    sayac4 = 0
    sayac5=0
    op=15
    for nm in range(5):
        if((liste[9][nm].__eq__("|x|")) and (liste[9][op].__eq__("|x|"))):
            sayac5=sayac5+1
            op=op+1
    if(sayac5==5):
        print("\nbilet adedi 2. kategorideki boş koltuk adedini aşıyor.")
        print("rezervasyon yapılamadı")

        sayac3 = 1
        sayac4 = 1
        b = 0

    for f in range(10):
        for i in range(4,-1,-1):
            if (liste[f][i].__eq__("|-|")):
                e = f
                r = i
                sayac2 = 1
                break
        if (sayac2 == 1):
            break
        for j in range(15,20):
            if (liste[f][j].__eq__("|-|")):
                e = f
                r = j
                sayac2 = 1
                break
        if (sayac2 == 1):
            break
    while(b>0):
        b = b - 1
        if(r<5):
            liste[e][r] = "|x|"
            lie.append(e)
            lir.append(r)
            r = r -1
            if(b==0):
                break
            sayac = sayac + 1
        if(r>14):
            liste[e][r] = "|x|"
            lie.append(e)
            lir.append(r)
            r = r + 1
            if(b==0):
                break
            sayac = sayac + 1
        if(r<0):
            r=15
        if (r > 19):
            r = 4
            e = e + 1
            if (e > 9):
                print("\nbilet adedi 2. kategorideki boş koltuk adedini aşıyor.")
                print("rezervasyon yapılamadı")
                sayac3=1
                sayac4=1
                e=9
                r=19
                while(sayac>0):
                    if(r>14):

                        liste[e][r]="|-|"
                        r=r-1
                        sayac=sayac-1
                        b=0
                    if(r<5):

                        liste[e][r]="|-|"
                        r=r+1
                        sayac=sayac-1
                        b=0
    if (sayac3 == 0):
        print("Reverze edilen koltuklar(sira-koltuk):", end=" ")
        for hj in range(len(lie)):
            print("{}-{}".format(lie[hj] + 1, lir[hj] + 1), end=" ")

    print("\n")

def kategori3(b):                  #kategori 3 için bilet kesim işlemlerini yapan fonksiyon
    sayac = 0
    e = 0
    r = 0
    sayac2 = 0
    lie=[]
    lir=[]
    sayac3=0
    global sayac4
    sayac4 = 0
    sayac5 = 0

    for nm in range(5, 15):
        if (liste[19][nm].__eq__("|x|")):
            sayac5 = sayac5 + 1
    if (sayac5 == 10):
        print("\nbilet adedi 3. kategorideki boş koltuk adedini aşıyor.")
        print("rezervasyon yapılamadı")
        sayac3 = 1
        sayac4 = 1
        b = 0

    for j in range(10,20):
        for z in range(5, 15):
            if (liste[j][z].__eq__("|-|")):
                e = j
                r = z
                sayac2 = 1
                break
        if (sayac2 == 1):
            break

    while (b > 0):
        b = b - 1
        liste[e][r] = "|x|"
        lie.append(e)
        lir.append(r)
        r = r + 1
        if(b==0):
            break

        sayac = sayac + 1
        if (r > 14):
            r = 5
            e = e + 1
            if (e > 19):
                print("\nbilet adedi 3. kategorideki boş koltuk adedini aşıyor.")
                print("rezervasyon yapılamadı")
                sayac3=1
                sayac4=1
                e=19
                r=14
                while (sayac > 0):

                    liste[e][r] = "|-|"
                    r = r - 1
                    sayac=sayac-1
                    b=0

    if (sayac3 == 0):
        print("Reverze edilen koltuklar(sira-koltuk):", end=" ")
        for hj in range(len(lie)):
            print("{}-{}".format(lie[hj] + 1, lir[hj] + 1), end=" ")

    print("\n")

def kategori4(b):               #kategori 4 için bilet kesim işlemlerini yapan fonksiyon
    e = 0
    r = 0
    sayac = 0
    sayac2 = 0
    lie=[]
    lir=[]
    sayac3=0
    global sayac4
    sayac4 = 0
    sayac5 = 0
    op = 15
    for nm in range(5):
        if ((liste[9][nm].__eq__("|x|")) and (liste[9][op].__eq__("|x|"))):
            sayac5 = sayac5 + 1
            op = op + 1
    if (sayac5 == 5):
        print("\nbilet adedi 4. kategorideki boş koltuk adedini aşıyor.")
        print("rezervasyon yapılamadı")

        sayac3 = 1
        sayac4 = 1
        b = 0

    for f in range(10,20):
        for i in range(4, -1, -1):
            if (liste[f][i].__eq__("|-|")):
                e = f
                r = i
                sayac2 = 1
                break
        if (sayac2 == 1):
            break
        for j in range(15, 20):
            if (liste[f][j].__eq__("|-|")):
                e = f
                r = j
                sayac2 = 1
                break
        if (sayac2 == 1):
            break
    while (b > 0):
        b = b - 1
        if (r < 5):
            liste[e][r] = "|x|"
            lie.append(e)
            lir.append(r)
            r = r - 1
            if(b==0):
                break
            sayac = sayac + 1
        if (r > 14):
            liste[e][r] = "|x|"
            lie.append(e)
            lir.append(r)
            r = r + 1
            if(b==0):
                break
            sayac = sayac + 1
        if (r < 0):
            r = 15
        if (r > 19):
            r = 4
            e = e + 1
            if (e > 19):
                print("\nbilet adedi 4. kategorideki boş koltuk adedini aşıyor.")
                print("rezervasyon yapılamadı")
                sayac3=1
                sayac4=1
                e=19
                r=19
                while(sayac>0):
                    if(r>14):

                        liste[e][r]="|-|"
                        r=r-1
                        sayac=sayac-1
                        b=0
                    if(r<5):

                        liste[e][r]="|-|"
                        r=r+1
                        sayac=sayac-1
                        b=0
    if (sayac3 == 0):
        print("Reverze edilen koltuklar(sira-koltuk):", end=" ")
        for hj in range(len(lie)):
            print("{}-{}".format(lie[hj] + 1, lir[hj] + 1), end=" ")

    print("\n")

while True:
    print("*" * 16)
    print("**  ANA MENÜ  **")
    print("*" * 16)
    print("1. Rezervasyon\n2. Salonu Yazdır\n3. Yeni Etkinlik\n4.Toplam Ciro\n0. Çıkış")
    print("*" * 16)

    a = int(input("Seçiminiz:"))
    if(a==1):

        k=int(input("Kategori(1-4):"))
        if (k > 4):                         #kategori değeri olarak geçersiz sayı girme durumu kontrolu
            print("kategori sınırını aştınız.")
            continue
        b=int(input("Bilet Adedi(1-10):"))

        if(b>int(dosyaicbilgi[0][1])):           #bilet değeri olarak geçersiz sayı girme durumu kontrolu
            print("izin verilen maksimum sayıdan dafa fazla bilet seçtiniz.")
            continue

        if (k == 1):                        #kategori 1 için bilet kesim işmleri için fonksiyonu çağırır.
            kategori1(b)

        if (k == 2):                        #kategori 2 için bilet kesim işmleri için fonksiyonu çağırır.
            kategori2(b)

        if (k == 3):                        #kategori 3 için bilet kesim işmleri için fonksiyonu çağırır.
            kategori3(b)

        if (k == 4):                        #kategori 4 için bilet kesim işmleri için fonksiyonu çağırır.
            kategori4(b)

        if(sayac4==0):                      #kategoride geçerli boş koltuk varsa ücret basmayı kontrol eder

            if (b <= int(dosyaicbilgi[0][1])):

                if (k == int(dosyaicbilgi[1][0])):            #kategori 1 için bilet kesim tutarını hesaplar
                    yt=5
                    fiyat = int(dosyaicbilgi[1][1])
                    while(k==int(dosyaicbilgi[yt][0])):
                        ucretHesaplama(yt)
                        yt=yt+1
                    if(sayac6==0):
                        print("indirim uygulanmadı.")
                        print("bilet adedi:",b,"toplam tutar:",(b*fiyat))


                if (k == int(dosyaicbilgi[2][0])):            #kategori 2 için bilet kesim tutarını hesaplar
                    fiyat = int(dosyaicbilgi[2][1])
                    yt=7
                    while (k == int(dosyaicbilgi[yt][0])):
                        ucretHesaplama(yt)
                        yt = yt + 1
                    if (sayac6 == 0):
                        print("indirim uygulanmadı.")
                        print("bilet adedi:", b, "toplam tutar:", (b * fiyat))

                if (k == int(dosyaicbilgi[3][0])):            #kategori 3 için bilet kesim tutarını hesaplar
                    fiyat = int(dosyaicbilgi[3][1])
                    yt=9
                    while (k == int(dosyaicbilgi[yt][0])):
                        ucretHesaplama(yt)
                        yt = yt + 1
                    if (sayac6 == 0):
                        print("indirim uygulanmadı.")
                        print("bilet adedi:", b, "toplam tutar:", (b * fiyat))

                if (k == int(dosyaicbilgi[4][0])):            #kategori 4 için bilet kesim tutarını hesaplar
                    fiyat = int(dosyaicbilgi[3][1])
                    yt=10
                    while (k == int(dosyaicbilgi[yt][0])):
                        ucretHesaplama(yt)
                        yt = yt + 1
                        if(yt==12):
                            break
                    if (sayac6 == 0):
                        print("indirim uygulanmadı.")
                        print("bilet adedi:", b, "toplam tutar:", (b * fiyat))

    if(a==2):                                   #salonun en son halini bastırır
        for satir in range(20):
            for sutun in range(20):
                print(liste[satir][sutun],end=" ")
                if(sutun==19):
                    print("\n")

    if(a==3):                                   #salonu yeni etkinliğe hazırlar
        for satir2 in range(20):
            for sutun2 in range(20):
                liste[satir2][sutun2]="|-|"
        netucretkategori[0]=0
        netucretkategori[1]=0
        netucretkategori[2]=0
        netucretkategori[3]=0

    if(a==4):                                   #bilet kesimlerinden sonra ciroları gösterir
        print("toplam ciro:",netucretkategori[0] + netucretkategori[1] + netucretkategori[2] + netucretkategori[3])
        print("1. kategori ciro:",netucretkategori[0])
        print("2. kategori ciro:", netucretkategori[1])
        print("3. kategori ciro:", netucretkategori[2])
        print("4. kategori ciro:", netucretkategori[3])
    if(a==0):                                   #programdan çıkmayı sağlar
        break;
