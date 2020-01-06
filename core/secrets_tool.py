# -*- coding: utf-8 -*-
__author__ = "yangtao"
import random
import os
import sys




def encrypt(src_str):
    src_bytearray = bytearray(str(src_str).encode("utf-8"))
    src_bytearray_len = len(src_bytearray)
    encrypted_bytearray = bytearray(src_bytearray_len * 3)

    bytearray_index = 0
    for i in range(0, src_bytearray_len):
        src_byte = src_bytearray[i]
        salt_byte = random.randint(33, 100)
        src_byte_integer = src_byte // 10 + salt_byte
        src_byte_remainder = src_byte % 10 + salt_byte

        encrypted_bytearray[bytearray_index] = src_byte_integer
        encrypted_bytearray[bytearray_index + 1] = salt_byte
        encrypted_bytearray[bytearray_index + 2] = src_byte_remainder
        bytearray_index += 3

    return encrypted_bytearray.decode("utf-8")


def decrypt(encrypted_str):
    encrypted_bytearray = bytearray(str(encrypted_str).encode("utf-8"))
    src_bytearray = bytearray(len(encrypted_bytearray) // 3)

    bytearray_index = 0
    for i in range(0, len(src_bytearray)):
        src_byte_integer = encrypted_bytearray[bytearray_index]
        salt_byte = encrypted_bytearray[bytearray_index + 1]
        src_byte_remainder = encrypted_bytearray[bytearray_index + 2]
        bytearray_index += 3

        src_byte = (src_byte_integer - salt_byte)*10 + (src_byte_remainder - salt_byte)
        src_bytearray[i] = src_byte

    return src_bytearray.decode("utf-8")


class Authenticator():
    def __init__(self, aut_file = None):
        if not aut_file:
            self.aut_file = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "aut")
        else:
            self.aut_file = aut_file
        aut_path = os.path.dirname(self.aut_file)
        if not os.path.exists(aut_path):
            os.makedirs(aut_path)

    def write_encrypt_code(self, user_name, password):
        user_code = encrypt(user_name)
        password_code = encrypt(password)
        encrypt_code = "%s %s" % (user_code, password_code)
        with open(self.aut_file, "w") as f:
            f.write(encrypt_code)

    def read_encrypt_code(self):
        if os.path.exists(self.aut_file):
            with open(self.aut_file, "r") as f:
                encrypt_code = f.readline()
                try:
                    code_split = encrypt_code.split(" ")
                    user_name = decrypt(code_split[0])
                    password = decrypt(code_split[-1])
                    return user_name, password
                except Exception as e:
                    print(e)
        return None, None

    def login(self, reload=False, username_prompt = "Name", password_prompt = "Password"):
        if not reload:
            user_name, password = self.read_encrypt_code()
            if user_name and password:
                return user_name, password

        # 输入账户密码
        user_name = input("%s: " % username_prompt)
        password = input("%s: " % password_prompt)
        self.write_encrypt_code(user_name, password)
        return user_name, password




if __name__ == "__main__":
    aa = encrypt("SG#yt@10")
    print(decrypt(aa))