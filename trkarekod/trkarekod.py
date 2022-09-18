import json
from typing import Union
from enum import Enum


class BicimGostergesi(str, Enum):
    # (str, Enum) olayini anla
    BKM_KKF = "99"
    ATM_KKF = "98"
    FAST_KKF = "96"

class UzunKarekod:
    """
    Uzun Karekod Formati TODO
    """

    def __init__(self) -> None:
        # ...
        raise NotImplemented


class KisaKarekod:
    """
    Kisa Karekod Formati TODO
    """

    def __init__(self) -> None:
        self.bicim_gostergesi = None
        self.uretici_kodu = None
        self.referans_numarasi = None
        self.proof = None
        self.crc = None
        self.raw = None


class ATMKarekod:
    """
    Atm Karekod Formati
    """

    def __init__(self, uretici_kodu, atm_data, raw) -> None:
        self.bicim_gostergesi = BicimGostergesi.ATM_KKF
        self.uretici_kodu = uretici_kodu
        self.atm_data = atm_data
        self.raw = raw

    # json serialisation
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    # type hinting'i string olarak vermek ise yaradi, sebebi ne acaba
    def from_string(atm_karekod_str: str) -> 'ATMKarekod':
        uretici_kodu = atm_karekod_str[2:6]
        atm_data = atm_karekod_str[6:]
        return ATMKarekod(uretici_kodu, atm_data, atm_karekod_str)


def parse(payload: str) -> Union[ATMKarekod, KisaKarekod]:
    # 1. karekod tipine karar ver
    # 2. karekod'u validate et
    # 3. karekod'u class'ina parse et
    if not isinstance(payload, str):
        raise TypeError("Karekod payload'i string olmali")
    switch=SwitchBicimGostergesi()
    return switch.bicimGostergesi(payload)
    
class SwitchBicimGostergesi:
    def bicimGostergesi(self,payload:str)->Union[ATMKarekod, KisaKarekod]:
        default="Bilinmeyen Biçim Göstergesi"
        return getattr(self,'case_'+str(payload[:2]),lambda:default)(payload)
    def case_99(self,payload:str):
        return
    def case_98(self,payload:str)-> 'ATMKarekod':
        if len(payload) < 7 or len(payload) > 220:  # hicbir value icermeyen payload
            raise ValueError("Karekod uzunlugu gecersiz")
        return ATMKarekod.from_string(payload)
    def case_96(self,payload:str):
        return
