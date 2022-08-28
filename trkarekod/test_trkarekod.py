from .trkarekod import parse


def test_atm_karekod():
    atm_kk = "98080012345678901201234567890123456789"
    kk = parse(atm_kk)
    print(kk.toJSON())
