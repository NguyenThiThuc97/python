# def _div(a, b):
#     try :
#         return str(a / b)
#     except ZeroDivisionError:
#         return "Error!"
# print("Chia hai so:")
# a = int(input("Nhap a:"))
# b = int(input("Nhap b:"))
# print(_div(a, b))

'''
1. Bat nhieu exception
try :
    # code
except (ZeroDivisionError, RuntimeError):
    # code
2. Khai bao nhieu exception
try :
    # code
except ZeroDivisionError:
    # code
except RuntimeError:
    # code
3. Long cac khoi exception
try :
    # code
except ZeroDivisionError:
    try :
        # code
    except StandardError:
        # code
except RuntimeError:
    # code
4. Finally
try:
    # code
except:
    # code
finally:
    # code
'''

'''
Xay dung mot exception
De tao mot exception thi bat buoc exception nay phai duoc ke thua tu lop Exception
'''
class DemoException(Exception):
    def __init__(self, value):
        print(value)
def _div(a, b):
    if (b == 0):
        raise DemoException("b khac 0")
    return a /b
print("Chia hai so:")
a = int(input("Nhap a:"))
b = int(input("Nhap b:"))
print(_div(a, b))
