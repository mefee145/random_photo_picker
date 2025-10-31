import os, random, subprocess

klasor = r"C:\Users\muham\Desktop\EFE\ÖZEL!\ADAYLAR"

uzantilar = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

foto_listesi = [f for f in os.listdir(klasor) if f.lower().endswith(uzantilar)]

if foto_listesi:
    secilen = random.choice(foto_listesi)
    tam_yol = os.path.join(klasor, secilen)
    print(f"Seçilen Fotoğraf:{tam_yol}")
    subprocess.run(["start", "", tam_yol], shell=True)
else:
    print("Hata: Fotoğraf bulunamadı!")