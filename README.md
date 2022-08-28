# trkarekod.py

trkarekod standardini impelment etmeye calisan python paketi.

Yukleme

```sh
git clone https://github.com/mrkaurelius/trkarekod.py
cd trkaredkod.py
pip install .
```

Test

```sh
pytest -rP
```

CLI tool

```sh
$ trkarekod 98080012345678901201234567890123456789
{
    "atm_data": "12345678901201234567890123456789",
    "bicim_gostergesi": "98",
    "raw": "98080012345678901201234567890123456789",
    "uretici_kodu": "0800"
}
```

## Kaynak Dokumanlar

internetten erişilebilen resmi dokümanlar: [Rehber Dokumani](https://www.tcmb.gov.tr/wps/wcm/connect/0ed756c3-a6ef-4043-88b7-63bdc3b86752/BKM+%28Kartl%C4%B1+%C3%96demeler%29+TR+Karekod+Teknik+%C4%B0lke+ve+Kurallar%C4%B1+Rehberi.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-0ed756c3-a6ef-4043-88b7-63bdc3b86752-nrmIcJA), [Ilke ve Kurallar Dokumani](https://www.tcmb.gov.tr/wps/wcm/connect/889054f9-abae-4912-b2c9-e8c4f611ab44/%C3%96deme+Hizmetlerinde+TR+Karekodun+%C3%9Cretilmesi+ve+Kullan%C4%B1lmas%C4%B1+Hakk%C4%B1nda+Y%C3%B6netmelik.pdf?MOD=AJPERES). Daha guncel oldugu icin Rehber Dokuman baz alinmistirl.
