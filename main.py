import os,vlc,time,random

muzik_listesi = []
anahtar = []

with os.scandir("set the music folder") as muzikler:
    for muzik in muzikler:
        if muzik.name.endswith("mp3"):
            muzik_listesi.append(str(muzik).replace("'","").split(" ")[1].split(".mp3")[0])
            anahtar.append(str(len(muzik_listesi)))

anahtar_deger = dict(zip(anahtar,muzik_listesi))
print("\n")

for anahtar,deger in anahtar_deger.items():
    print(f"[{anahtar}] - {deger}")

secim = input("\nseçim = ")

for anahtar,deger in anahtar_deger.items():

    if secim==anahtar:
        sarki = vlc.MediaPlayer(f"set the music folder/{deger}.mp3")
        print(f"çalınan şarkı = {deger}".title().replace("-"," "))

        sarki.play()
        time.sleep(0.1)
        while sarki.is_playing():
            time.sleep(1)
        sarki.stop()

        while True:
            random_muzik = random.randint(1,(len(muzik_listesi)))
            isim = anahtar_deger[str(random_muzik)]
            print(f"çalınan şarkı = {isim}".title().replace("-"," "))
            sarki = vlc.MediaPlayer(f"set the music folder/{isim}.mp3")
            sarki.play()
            time.sleep(0.1)

            while sarki.is_playing():
                time.sleep(1)

            sarki.stop()
