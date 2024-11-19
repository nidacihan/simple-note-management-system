# Basit Not Yönetim Sistemi

def not_yonetim_sistemi():

    ogrenciler  = {}


    def menu_goster():
        print("\nnot yönetim sistemi")

        print("\n1. öğrenci ekle")
        print("2. tüm öğrencileri görüntüle")
        print("3. ortalama not hesapla")
        print("4. en yüksek ve en düşük notu bul")
        print("5. çıkış")

        print("\nnot yönetim sistemine hoşgeldiniz.")


    while True:
        secim = input("\nSeçiminizi yapın (1-5, 'm' ile menüyü tekrar göster):")




        if secim == '1':
            isim  = input("öğrencinin adını girin")
            try:
                notu = float(input("öğrencinin notunu girin:"))
                ogrenciler[isim] = notu
                print(f"{isim} başarıyla eklendi.")
            except ValueError:
                print("hata: lütfen geçerli bir not girin.")
        elif secim == '2':
            if ogrenciler:
                print("\nÖğrenciler ve notları:")
                for isim, notu in ogrenciler.items():
                    print(f"{isim}: {notu}")
            else:
                print("henüz hiçbir öğrenci eklenmedi.")

        elif secim == '3':
            if ogrenciler:
                ortalama = sum(ogrenciler.values()) / len(ogrenciler)
                print(f"sınıfın ortalama notu: {ortalama:.2f}")
            else:
                print("hesaplama yapmak için önce öğrenci ekleyin.")

        elif secim == '4':
            if ogrenciler:
                en_yuksek = max(ogrenciler.values())
                en_dusuk = min(ogrenciler.values())
                print(f"en yüksek not: {en_yuksek}")
                print(f"en düşük not: {en_dusuk}")
            else:
                print("hesaplama yapmak için önce öğrenci ekleyin.")

        elif secim == '5':
            print('çıkıl yapılıyor.')
            break

        elif secim == 'm':
            menu_goster()
        else:
            print("geçersiiz seçim, tekrar deneyin.")

not_yonetim_sistemi()