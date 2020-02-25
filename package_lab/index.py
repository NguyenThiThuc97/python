'''
Package trong python la mot thu muc chua mot hoac nhieu module hay cac package khac nhau
No dc tao ra nham muc dich phan bo cac module
1. Build package
Ten thu muc la ten package va trong thu muc phai chua file co ten __init__.py (se duoc goi dau tien khi import package)
'''
import demopackage.demomodule as demo
import demopackage.childpackage.childmodule as demo1

demo._say_hello()
demo._say_goodbye()
demo1._child_hello()