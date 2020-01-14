# -*- coding: utf-8 -*-
__author__ = "yangtao"


import re


  

def get_max_ver_num(name_list):
    ver_list = []
    for n in name_list:
        re_result = re.search("(?P<ver>v|V)(?P<num>\d+)", n)
        if re_result:
            ver_list.append(re_result.group("num"))
    if ver_list:
        ver_list.sort()
        return int(ver_list[-1])
    else:
        return 0




if __name__ == "__main__":
    aa = ['WTS 特效规范191014.v01', '879151_1.v02', '1_sUI4nkPfH0wevBQMb29cnQ.v04', '8d0c415f65118618b763924029f0d9b5.v0001']
    print(get_max_ver_num(aa))