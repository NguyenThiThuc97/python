# 1. Map()
def _multiply(x):
    return x *x
result = map(_multiply, [1, 2, 3])
print(list(result))

result1 = map(lambda x: x * x, [4, 6, 7])
print(list(result1))

result2 = map(lambda x, y: x + "-" + y, ["Rose", "Lily", "3"], ["1", "2"])
print(list(result2))

# 2. Filter(): tra ve cac gia tri ma dieu kien trong function duoc chap nhan

result3 = filter(lambda x : x % 2, [0,1,2,3,4,5,6])
print(list(result3))