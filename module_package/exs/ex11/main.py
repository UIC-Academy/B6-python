from prvt import *

print(iampublic(), _iamprvt())

try:
    import eshmat
    print(dir(eshmat))
except ModuleNotFoundError:
    print("No module named eshmat, Eshmat!")