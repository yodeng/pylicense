# coding:utf-8

import os
import json
import datetime

from create_license import AESEncryptDecrypt, GetMacAddress, pprint

__all__ = ["check_license"]


def calibrator(lic_file):

    KEY = "nX4rAqc9mi81Duog5UMbfVI0v3YPOkdZ"

    aes_crypt = AESEncryptDecrypt(KEY)
    obj = GetMacAddress()
    mac = obj.mac()                             # 本机的mac地址
    encrypt_code = aes_crypt.encrypt(mac)       # AES加密后的mac

    if os.path.isfile(lic_file):
        with open(lic_file) as lic:
            encrypt_data = lic.read().strip("\n")
            lic.close()
    else:
        print(pprint(
            'liscese file not exists, please contact admin and send "%s" for access' % encrypt_code, mode='bold', fore='red'))
        return False
    try:
        decrypt_data = aes_crypt.decrypt(encrypt_data)
    except Exception as e:
        decrypt_data = '{}'
    dict_data = json.loads(decrypt_data)

    if dict_data.get('unique_code') != encrypt_code:
        print(pprint('liscese not access on this host machine, please contact admin and send "%s" for access' %
                     encrypt_code, mode='bold', fore='red'))
        return False

    if dict_data.get('life_time') is True:
        return True
    else:
        try:
            today_date = datetime.datetime.today()
            start_date = datetime.datetime.strptime(
                dict_data['start_date'], "%Y-%m-%d")
            end_date = datetime.datetime.strptime(
                dict_data['end_date'], "%Y-%m-%d")
            if dict_data.get('life_time') is False and start_date <= today_date <= end_date:
                return True
            else:
                print(pprint('license out of data, please contact admin and send "%s" for new access' %
                             encrypt_code, mode='bold', fore='red'))
                return False
        except Exception as e:
            pass
    return False


def check_license(lic_file):
    lic_path = lic_file
    return calibrator(lic_path)
