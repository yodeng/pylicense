#! /usr/bin/env python
# coding:utf-8

import os
import json
import datetime

from check_license import check_license
from create_license import GetMacAddress, AESEncryptDecrypt, pprint

from license_info import IP, KEY, DATA, LICENSEFILE


def creatLicense(lic_file, key, dict_data=None):
    if dict_data is None:
        dict_data = {}
    data = json.dumps(dict_data)
    aes_crypt = AESEncryptDecrypt(key=key)
    encrypt_data = aes_crypt.encrypt(data)

    with open(lic_file, "w") as lic:
        lic.write(encrypt_data+"\n")
    print(pprint("license file path: %s, please copy this file to client." %
                 lic_file, mode='bold'))


def main():
    lic_file = LICENSEFILE
    macinfo = GetMacAddress(ip=IP)
    mac = macinfo.mac()
    encrypt_code = AESEncryptDecrypt(KEY).encrypt(mac)

    DATA['unique_code'] = encrypt_code
    creatLicense(lic_file, KEY, dict_data=DATA)

    print('license assess：%s' % check_license(lic_file))


if __name__ == '__main__':
    main()
