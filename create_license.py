# coding:utf-8

import base64
import socket
import netifaces

from Crypto.Cipher import AES


def add_to_16(v):
    while len(v) % 16 != 0:
        v = v + "\0"
    return v


class AESEncryptDecrypt(object):
    def __init__(self, key):
        self.__key = add_to_16(key)
        self.__mode = AES.MODE_ECB

    def encrypt(self, data):
        """
        str =(aes编码)=> bytes =(base64编码)=> bytes =(utf-8解码)=> str
        :param data:
        :return:
        """
        data = add_to_16(data)
        cipher = AES.new(self.__key, self.__mode)

        # encrypt_data:<class 'bytes'>  AES编码
        encrypt_data = cipher.encrypt(data)
        # encrypt_data:<class 'bytes'>  base64编码，参数为bytes类型
        encrypt_data = base64.b64encode(encrypt_data)
        # encrypt_data:<class 'str'>  使用utf-8解码成字符串
        encrypt_data = encrypt_data.decode('utf-8')
        return encrypt_data

    def decrypt(self, encrypt_data):
        """
        str =(base64解码)=> bytes =(aes解码)=> bytes =(utf-8编码)=> str
        :param encrypt_data:
        :return:
        """
        cipher = AES.new(self.__key, self.__mode)

        encrypt_data = base64.b64decode(encrypt_data)  # <class 'bytes'>
        decrypt_data = cipher.decrypt(encrypt_data)  # <class 'bytes'>
        decrypt_data = decrypt_data.decode('utf-8')  # <class 'str'>
        decrypt_data = decrypt_data.rstrip('\0')
        return decrypt_data


class GetMacAddress(object):
    def __init__(self, ip=""):
        self.ip = ip
        self.__mac = ''

    def get_ip_address(self):
        if self.ip:
            return self.ip
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('114.114.114.114', 80))
            self.ip = s.getsockname()[0]
        finally:
            s.close()
            return self.ip

    def get_mac_address(self):
        ip = self.get_ip_address()
        for i in netifaces.interfaces():
            addrs = netifaces.ifaddresses(i)
            try:
                if_mac = addrs[netifaces.AF_LINK][0]['addr']
                if_ip = addrs[netifaces.AF_INET][0]['addr']
                if if_ip == ip:
                    self.__mac = if_mac
                    break
            except KeyError:
                pass

    def mac(self):
        self.get_mac_address()
        return self.__mac


def pprint(strings, length=0, justify="", fill="", mode='', fore='', back=''):
    '''
    length:  指定字符串占的位置长度, 默认等于字符串的长度
    justify:  对其方式, ["r","m","l"]  默认左对齐
    fill: 填充字符,只允许单个字符   默认一个空格
    '''
    STYLE = {
        'fore': {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37},
        'back': {'black': 40, 'red': 41, 'green': 42, 'yellow': 43, 'blue': 44, 'purple': 45, 'cyan': 46, 'white': 47},
        'mode': {'mormal': 0, 'bold': 1, 'underline': 4, 'blink': 5, 'invert': 7, 'hide': 8},
        'default': {'end': 0},
    }
    alig_justify = {"l": "<", "r": ">", "m": "^"}
    mode = '%s' % STYLE["mode"].get(mode, "")
    fore = '%s' % STYLE['fore'].get(fore, "")
    back = '%s' % STYLE['back'].get(back, "")
    style = ';'.join([s for s in [mode, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end = '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style, ("{:%s%s%d}" % (fill, alig_justify.get(justify, "<"), length)).format(strings), end)
