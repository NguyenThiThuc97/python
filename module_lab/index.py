#1. import module1, module2,...

# import math

# a = 1.5987

# print(math.ceil(a))
# print(math.floor(a))

#2. khi khong muon import tat ca cac method trong module
# from modules import something, something2,...

#3. khi muon import tat ca nhung gi trong module co va cho phep:
# from math import *

# a = 1.5987

# print(ceil(a))
# print(floor(a))

#4. Build module
# import math_plus
# print(math_plus.get_sum(4, 5))

# 5. Luu y: khi su dung: from ... import * thi python se ko import dc cac doi tuong co ten bat dau bang ki tu (_).
# Trong truong hop nay, neu muon import duoc cac doi tuong thi phai chi dich danh cac doi tuong do.
# from math_plus import _get_name
# print(_get_name("Thuc"))

# 6. Import module in folder:
# Mac dinh thi Python chi load cac module he thong cua no va cac module o cung cap vs thu muc hien tai.
# Neu muon python load module o nhung thu muc nao thi can phai cau hinh trong sys.path
# De them thu muc can load: su dung phuong thuc append() trong module sys.path.
import os, sys
# get modules path in current project
lib_path = os.path.abspath(os.path.join("modules"))
# add module into system
sys.path.append(lib_path)
from methods import _get_age
print(_get_age(15))