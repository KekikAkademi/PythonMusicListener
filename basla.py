
from AYAR   import MUZIK_DIZINI
from os     import listdir
from random import shuffle, choice
from vlc    import MediaPlayer
from time   import sleep

muzikler = [dosya.replace('.mp3', '') for dosya in listdir(f'{MUZIK_DIZINI}/.') if dosya.endswith('.mp3')]

def sarki_cal(sarki_adi):
    global muzikler

    _vlc = MediaPlayer(f"{MUZIK_DIZINI}{sarki_adi}.mp3")

    _vlc.play()
    sleep(.1)
    print(f"\n\nçalan şarkı = {sarki_adi}".replace("-"," ").title())
    while _vlc.is_playing():
        sleep(1)

    _vlc.stop()

    muzikler.remove(sarki_adi)

print("\n\tSenin Müziklerin;\n\n")

for say, sarki in enumerate(muzikler):
    print(f'[{say}] - {sarki.replace("-"," ").title()}')

secim = int(input("\nSeçim = "))

sarki_cal(muzikler[secim])

shuffle(muzikler)

while muzikler:
    sarki_cal(choice(muzikler))