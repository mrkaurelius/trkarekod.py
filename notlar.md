# Notlar

Dokumanda birden cok kez birbiri ile celiskili tanimlar var yada ben yanlis anliyorum

- Karekod Biçim Göstergesi vs Alan kodu
- Karekod formatlari
  - Kisa Karekod Formati (KKF)
  - Uzun Karekod Formati (UKF)
  - ATM Karekod Yapisi
    - tanimlarda yok ama 6.1.4 de verilmis

- Nesne tipleri
  - Basit veri nesnesi
    - tarih, tutar, referans gibi tek bir bilgiyi saklar
  - Veri sablonu nesnesi
    - basit veri nesneleri yada veri sablonu nesneleri (nested) saklar

Her bir nesne 3 bolumden olusur

- Alan kodu
  - 00 ve 99 arasinda, nesnenin kimligini belirtir (magic number)
- Uzunluk
  - 00 ve 99 arasinda, nesnenin uzunlugunu belirtir
- Veri degeri
  - 00 ve 99 uzunlugunda nesnenin degeri

Karekod icindeki verilerin tipleri

- Karakter Dizgizi (K)
  - UTF-8 karakterlerinden olusan dizgi
- Ozel Alfa Numerik (OAN)
  - alfanumerik ve noktalama isaretleri icerir
- Numerik (N)
  - Sadece rakamlari icerir, OAN'in alt kumesi

Karekod veri organizasyonu icerisindeki nesnelerin bulunma durumu

- Zorunlu (Z)
- Istege Bagli (I)
- Kosullu (K)

Karekodun ilk veri nesnesi olan Karekod Biçim Göstergesi, karekodun kullanım modeline uygun türünü
ve bu doğrultuda geri kalan verinin yapısını, gösterimini ve sürümünü belirtmektedir. Uygulamalar,
karekodda ilk olarak bu nesneyi okuyarak tüm veriyi ayrıştırırlar

### Ornekler

020820200530 alan kodu 02, uzunlugu 08 veri degeri 20200530 olan bir nesne

### Karekod Tipleri

kisa karekod ve atm karekod hemen yapilabilir, ukf icin biraz ugrasmak lazim

#### Kisa Karekod

referans numarasina arbitrary birsey konulabilir mi ? kk referans numarasi incremental olamali.

```
| kk bicim | kk uretici kodu | kk referans numarasi | kart kabul eden proof | crc |
```

### ATM Karekod

```
| kk bicim | kk uretici kodu | ATM data |
```

ATM data 0 214 arasinda, kart kabul eden kurulus kendi standartlarina gore olusturabilir (arbitrary)