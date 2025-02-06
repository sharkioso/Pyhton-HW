#!/usr/bin/env python
import sys
import math


def f0():
    return 1 / 0


def f1():
    a = [1, 4, 3]
    b = 1
    return a + b


def f2():
    return 1 / 0


def f3():
    """
    РїРѕСЃР»Рµ РїРѕРёСЃРєР° РёРЅС„РѕСЂРјР°С†РёРё РІ РёРЅС‚РµСЂРЅРµС‚Рµ, СЏ РѕР±РЅР°СЂСѓР¶РёР», С‡С‚Рѕ СЌС‚Р° РѕС€РёР±РєР°-
    FloatingPointException РІ python СЃРµР№С‡Р°СЃ РЅРµ РёСЃРїРѕР»СЊР·СѓРµС‚СЃСЏ СЃС‚Р°РЅРґР°СЂС‚РЅС‹РјРё
    Р±РёР±Р»РёРѕС‚РµРєР°РјРё СЌС‚Рѕ СѓРєР°Р·Р°РЅРѕ РІ РґРѕРєСѓРјРµРЅС‚Р°С†РёРё
    https://docs.python.org/3/library/exceptions.html#FloatingPointError
    СЏ РЅР°С€РµР»С‡С‚Рѕ РѕРЅР° РёСЃРїРѕР»СЊР·СѓРµС‚СЃСЏ РІ Р±РёР±Р»РёРѕС‚РµРєРµ numPY, РЅРѕ СЏ С‚Р°Рє РїРѕРЅРёРјР°СЋ
    РјС‹ РїРѕР»СЊР·СѓРµРјСЃСЏ С‚РѕР»СЊРєРѕ СЃС‚Р°РЅРґР°СЂС‚РЅС‹РјРё Р±РёР±Р»РёРѕС‚РµРєР°РјРё.
    РќРёР¶Рµ СѓРєР°Р·Р°РЅ РєРѕРґ, РєРѕС‚РѕСЂС‹Р№ РєР°Рє СЏ РїРѕРЅРёРјР°СЋ РјРѕРі Р±С‹ РІС‹Р·РІР°С‚СЊ СЌС‚Сѓ РѕС€РёР±РєСѓ РІ
    РІРµСЂСЃРёРё РїРёС‚РѕРЅР° 3.1 РІ РґРѕРєСѓРјРµРЅС‚Р°С†РёРё РѕРїРёСЃР°РЅРѕ, С‡С‚Рѕ РѕРЅР° С‚Р°Рј РµС‰С‘ Р±С‹Р»Р°.

    return 1.0/0.0
    """
    raise FloatingPointError


def f4():
    return math.exp(1337)


def f5():
    return 1 / 0


def f6():
    assert 1 == 0


def f7():
    a = 1
    return a.__elclassico__


def f8():
    file = open("error.txt", 'r')
    return file


def f9():
    import mishaTetkin


def f10():
    a = [1, 4, 3]
    return a[1111]


def f11():
    a = [1, 4, 3]
    return a[1111]


def f12():
    a = {"a": 1, "d": 4, "c": 3}
    return a['b']


def f13():
    return mishaTetkin


def f14():
    eval("0+_!@()!@!)@($#1")


def f15():
    return int("РЅРѕР»СЊ")


def f16():
    string = "misha TГ©tkin"
    return string.encode('ascii')


def check_exception(f, exception):
    try:
        f()
    except exception:
        pass
    else:
        print("Bad luck, no exception caught: %s" % exception)
        sys.exit(1)


check_exception(f0, BaseException)
check_exception(f1, Exception)
check_exception(f2, ArithmeticError)
check_exception(f3, FloatingPointError)
check_exception(f4, OverflowError)
check_exception(f5, ZeroDivisionError)
check_exception(f6, AssertionError)
check_exception(f6, AssertionError)
check_exception(f7, AttributeError)
check_exception(f8, EnvironmentError)
check_exception(f9, ImportError)
check_exception(f10, LookupError)
check_exception(f11, IndexError)
check_exception(f12, KeyError)
check_exception(f13, NameError)
check_exception(f14, SyntaxError)
check_exception(f15, ValueError)
check_exception(f16, UnicodeError)

print("Congratulations, you made it!")